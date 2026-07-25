"""Dynamic translation of larger content bodies (disease descriptions, Kids
Check-In content, symptom vocabulary) via the already-configured Anthropic
model. Falls back to None when the AI Assistant isn't configured or the
translation call fails, so callers can show English instead of crashing.

Results are cached to disk per language (data/translations/{lang}.json,
gitignored) so each language is only translated once per deployment.
"""

import json
from pathlib import Path

import streamlit as st

import rag

TRANSLATIONS_DIR = Path(__file__).parent / "data" / "translations"
TRANSLATE_MODEL = "claude-sonnet-5"
# The full bundle (32 conditions + Kids Check-In content + symptom vocabulary)
# translates to a large JSON blob — 8000 tokens was observed to truncate
# mid-response (stop_reason="max_tokens"), so this needs real headroom.
TRANSLATE_MAX_TOKENS = 24000
TRANSLATE_TIMEOUT_SECONDS = 300


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


def _build_source_bundle() -> dict:
    from health_data import DISEASES, build_symptom_pool
    from kids_data import KIDS_QUESTIONS, SAFETY_QUESTION, KIDS_THEMES

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

    questions = {q["key"]: q["prompt"] for q in KIDS_QUESTIONS}
    questions["safety"] = SAFETY_QUESTION["prompt"]

    themes = {
        key: {"title": theme["title"], "blurb": theme["blurb"], "tip": theme["tip"]}
        for key, theme in KIDS_THEMES.items()
    }

    return {
        "diseases": diseases,
        "symptoms": symptoms,
        "kids_questions": questions,
        "kids_themes": themes,
    }


def _extract_json(text: str) -> dict:
    text = text.strip()
    if text.startswith("```"):
        text = text.split("\n", 1)[1] if "\n" in text else text
        if text.endswith("```"):
            text = text.rsplit("```", 1)[0]
    return json.loads(text)


@st.cache_resource
def _translate_bundle_cached(lang: str, language_name: str):
    cached = _load_cache(lang)
    if cached is not None:
        return cached

    if not rag.is_configured():
        return None

    source = _build_source_bundle()
    client = rag.get_anthropic_client()

    prompt = (
        f"Translate every string value in this JSON object into {language_name}, for a "
        "physical- and mental-health symptom-checker app. Keep it natural, warm, and "
        "clinically accurate — this includes supportive mental-health text written for "
        "young people, so tone matters a great deal. "
        "Return ONLY valid JSON with the exact same keys and structure as the input "
        "(never translate or change any keys, only the string values). Do not add "
        "commentary, markdown fences, or explanation — JSON only.\n\n"
        f"{json.dumps(source, ensure_ascii=False)}"
    )

    try:
        response = client.messages.create(
            model=TRANSLATE_MODEL,
            max_tokens=TRANSLATE_MAX_TOKENS,
            messages=[{"role": "user", "content": prompt}],
            timeout=TRANSLATE_TIMEOUT_SECONDS,
        )
        text_blocks = [b.text for b in response.content if getattr(b, "type", None) == "text"]
        translated = _extract_json("\n".join(text_blocks))
    except Exception:
        return None

    if not isinstance(translated, dict) or "diseases" not in translated:
        return None

    _save_cache(lang, translated)
    return translated


def get_bundle(lang: str, language_name: str):
    """Return the translated content bundle for `lang`, or None if unavailable
    (English selected, AI Assistant not configured, or translation failed)."""
    if lang == "en":
        return None
    return _translate_bundle_cached(lang, language_name)
