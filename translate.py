"""Dynamic translation of larger content bodies (disease descriptions, Kids
Check-In content, Mental Health Check-In content, symptom vocabulary) via
the already-configured Anthropic model. Falls back to None when the AI
Assistant isn't configured or translation fails, so callers can show
English instead of crashing.

Results are cached to disk per language (data/translations/{lang}.json,
gitignored) so each language is only translated once per deployment. The
bundle is built from two separate API calls (diseases+symptoms is by far
the largest part; Kids/Mental-Health content is much smaller) so a
truncated or failed call only degrades that half instead of the whole
bundle.
"""

import json
from pathlib import Path

import streamlit as st

import rag

TRANSLATIONS_DIR = Path(__file__).parent / "data" / "translations"
TRANSLATE_MODEL = "claude-sonnet-5"
TRANSLATE_TIMEOUT_SECONDS = 300
# The disease+symptom blob is the bulk of the content (57 conditions, ~220
# symptom labels) — give it a large budget. Truncation was observed at
# lower values (stop_reason="max_tokens"), so this needs real headroom.
DISEASES_MAX_TOKENS = 32000
OTHER_MAX_TOKENS = 12000


def _cache_path(lang: str) -> Path:
    return TRANSLATIONS_DIR / f"{lang}.json"


def _load_cache(lang: str):
    path = _cache_path(lang)
    if not path.exists():
        return None
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return None


def _save_cache(lang: str, data: dict) -> None:
    TRANSLATIONS_DIR.mkdir(parents=True, exist_ok=True)
    with open(_cache_path(lang), "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)


def _build_disease_source() -> dict:
    from health_data import DISEASES, build_symptom_pool

    diseases = {
        name: {
            "name": name,
            "description": info["description"],
            "advice": info["advice"],
            "mayo_summary": info.get("mayo_summary", ""),
        }
        for name, info in DISEASES.items()
    }
    # Identity map so translated output keeps the canonical English symptom
    # as the key and the translated label as the value.
    symptoms = {symptom: symptom for symptom in build_symptom_pool(DISEASES)}
    return {"diseases": diseases, "symptoms": symptoms}


def _build_other_source() -> dict:
    from kids_data import KIDS_QUESTIONS, SAFETY_QUESTION, KIDS_THEMES
    from mental_health_data import (
        DEPRESSION_QUESTIONS,
        ANXIETY_QUESTIONS,
        SAFETY_QUESTION as MH_SAFETY_QUESTION,
        DEPRESSION_SEVERITY_BANDS,
        ANXIETY_SEVERITY_BANDS,
    )

    kids_questions = {q["key"]: q["prompt"] for q in KIDS_QUESTIONS}
    kids_questions["safety"] = SAFETY_QUESTION["prompt"]

    kids_themes = {
        key: {"title": theme["title"], "blurb": theme["blurb"], "tip": theme["tip"]}
        for key, theme in KIDS_THEMES.items()
    }

    mh_questions = {q["key"]: q["prompt"] for q in DEPRESSION_QUESTIONS + ANXIETY_QUESTIONS}
    mh_questions["safety"] = MH_SAFETY_QUESTION["prompt"]

    severity_labels = {
        label: label
        for _, _, label, _ in DEPRESSION_SEVERITY_BANDS + ANXIETY_SEVERITY_BANDS
    }

    return {
        "kids_questions": kids_questions,
        "kids_themes": kids_themes,
        "mh_questions": mh_questions,
        "mh_severity_labels": severity_labels,
    }


def _extract_json(text: str) -> dict:
    text = text.strip()
    if text.startswith("```"):
        text = text.split("\n", 1)[1] if "\n" in text else text
        if text.endswith("```"):
            text = text.rsplit("```", 1)[0]
    return json.loads(text)


def _translate_blob(source: dict, language_name: str, max_tokens: int):
    """Translate one JSON blob in a single API call. Returns a dict or None on any failure."""
    client = rag.get_anthropic_client()
    prompt = (
        f"Translate every string value in this JSON object into {language_name}, for a "
        "physical- and mental-health symptom-checker app. Keep it natural, warm, and "
        "clinically accurate — this includes supportive mental-health text written for "
        "young people and adults, so tone matters a great deal. "
        "Return ONLY valid JSON with the exact same keys and structure as the input "
        "(never translate or change any keys, only the string values). Do not add "
        "commentary, markdown fences, or explanation — JSON only.\n\n"
        f"{json.dumps(source, ensure_ascii=False)}"
    )
    try:
        response = client.messages.create(
            model=TRANSLATE_MODEL,
            max_tokens=max_tokens,
            messages=[{"role": "user", "content": prompt}],
            timeout=TRANSLATE_TIMEOUT_SECONDS,
        )
        text_blocks = [b.text for b in response.content if getattr(b, "type", None) == "text"]
        translated = _extract_json("\n".join(text_blocks))
    except Exception:
        return None

    if not isinstance(translated, dict):
        return None
    return translated


@st.cache_resource
def _translate_bundle_cached(lang: str, language_name: str):
    cached = _load_cache(lang)
    if cached is not None:
        return cached

    if not rag.is_configured():
        return None

    translated_diseases = _translate_blob(_build_disease_source(), language_name, DISEASES_MAX_TOKENS)
    translated_other = _translate_blob(_build_other_source(), language_name, OTHER_MAX_TOKENS)

    if translated_diseases is None and translated_other is None:
        return None

    merged = {}
    merged.update(translated_diseases or {})
    merged.update(translated_other or {})

    _save_cache(lang, merged)
    return merged


def get_bundle(lang: str, language_name: str):
    """Return the translated content bundle for `lang`, or None if unavailable
    (English selected, AI Assistant not configured, or translation failed)."""
    if lang == "en":
        return None
    return _translate_bundle_cached(lang, language_name)
