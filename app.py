import streamlit as st
from streamlit_js_eval import get_geolocation

import hospital_finder
import i18n
import rag
import translate
from health_data import (
    DISEASES,
    EMERGENCY_SYMPTOMS,
)
from kids_data import (
    KIDS_QUESTIONS,
    SAFETY_QUESTION,
    KIDS_THEMES,
    KIDS_RESOURCES,
)
from mental_health_data import (
    ANSWER_OPTIONS as MH_ANSWER_OPTIONS,
    DEPRESSION_QUESTIONS,
    ANXIETY_QUESTIONS,
    SAFETY_QUESTION as MH_SAFETY_QUESTION,
    DEPRESSION_SEVERITY_BANDS,
    ANXIETY_SEVERITY_BANDS,
    MENTAL_HEALTH_RESOURCES,
    severity_band,
)

st.set_page_config(
    page_title="Symptom Checker — Physical & Mental Health",
    page_icon="🩺",
    layout="wide",
)

# ------------------------------------------------------------- language ---

lang = st.sidebar.selectbox(
    i18n.t("en", "language_label"),
    options=list(i18n.LANGUAGES.keys()),
    format_func=lambda code: i18n.LANGUAGES[code],
    key="app_language",
)

# Dynamically translated content (disease data, Kids Check-In text, symptom
# vocabulary). None when English is selected, the AI Assistant isn't
# configured, or translation failed — callers fall back to English.
bundle = translate.get_bundle(lang, i18n.LANGUAGES[lang])
show_translation_note = lang != "en" and bundle is None


def translate_symptom(symptom: str) -> str:
    return (bundle or {}).get("symptoms", {}).get(symptom, symptom)


def localize_diseases(diseases: dict) -> dict:
    translated = (bundle or {}).get("diseases", {})
    localized = {}
    for name, info in diseases.items():
        info_t = translated.get(name, {})
        localized[name] = dict(info)
        localized[name]["display_name"] = info_t.get("name", name)
        localized[name]["description"] = info_t.get("description", info["description"])
        localized[name]["advice"] = info_t.get("advice", info["advice"])
        if info.get("mayo_summary"):
            localized[name]["mayo_summary"] = info_t.get("mayo_summary", info["mayo_summary"])
        localized[name]["symptoms"] = [translate_symptom(s) for s in info["symptoms"]]
    return localized


def localized_symptom_pool(localized_diseases: dict) -> list:
    pool = set()
    for info in localized_diseases.values():
        pool.update(info["symptoms"])
    pool.update(translate_symptom(s) for s in EMERGENCY_SYMPTOMS)
    return sorted(pool)


# Visual style: Mayo-inspired navy/blue palette with a futuristic gradient/glow treatment.
BADGE_COLORS = {
    "emergency": "#C8102E",
    "see_doctor": "#0067B1",
    "self_care": "#2E7D32",
}

st.markdown(
    f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;600;700;800&display=swap');

    html, body, [class*="css"] {{
        font-family: 'Roboto', -apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif;
    }}

    .stApp {{
        background: linear-gradient(180deg, #F5FAFF 0%, #FFFFFF 320px);
    }}

    .mc-topbar {{
        background: linear-gradient(90deg, #0B2D4D 0%, #0E3A66 55%, #0067B1 100%);
        color: #FFFFFF;
        margin: -1rem -1rem 0 -1rem;
        padding: 0.9rem 1.5rem;
        border-bottom: 3px solid #00C2FF;
        font-size: 1rem;
        font-weight: 700;
        letter-spacing: 0.06em;
        text-transform: uppercase;
        box-shadow: 0 2px 18px rgba(0, 103, 177, 0.28);
    }}
    .mc-breadcrumb {{
        margin: 0.75rem 0 0.25rem 0;
        color: #5B6B79;
        font-size: 0.85rem;
    }}

    h1, h2, h3 {{ color: #0B2D4D !important; font-weight: 800 !important; }}
    h1 {{
        background: linear-gradient(90deg, #0B2D4D 0%, #0067B1 55%, #00A6E0 100%);
        -webkit-background-clip: text;
        background-clip: text;
        -webkit-text-fill-color: transparent;
    }}
    a, a:visited {{ color: #0067B1; }}

    .stButton > button {{
        background: linear-gradient(90deg, #0067B1 0%, #0090D1 100%);
        color: #FFFFFF;
        border: none;
        border-radius: 8px;
        font-weight: 600;
        padding: 0.55rem 1.5rem;
        transition: box-shadow 0.2s ease, transform 0.2s ease;
        box-shadow: 0 2px 10px rgba(0, 103, 177, 0.25);
    }}
    .stButton > button:hover {{
        box-shadow: 0 4px 18px rgba(0, 144, 209, 0.45);
        transform: translateY(-1px);
    }}
    .stButton > button:disabled {{
        background: #C7D3DB;
        color: #FFFFFF;
        box-shadow: none;
        transform: none;
    }}

    section[data-testid="stSidebar"] {{
        background-color: #F4F6F8;
        border-right: 1px solid #E1E5E9;
    }}

    div[data-testid="stVerticalBlockBorderWrapper"] {{
        border-radius: 10px !important;
        border: 1px solid #E1E5E9 !important;
        box-shadow: 0 1px 3px rgba(11, 45, 77, 0.06);
        transition: box-shadow 0.2s ease;
    }}
    div[data-testid="stVerticalBlockBorderWrapper"]:hover {{
        box-shadow: 0 6px 24px rgba(0, 103, 177, 0.16);
    }}

    .stProgress > div > div > div > div {{
        background: linear-gradient(90deg, #0067B1, #00C2FF);
    }}

    .mc-badge {{
        display: inline-block;
        padding: 4px 12px;
        border-radius: 999px;
        font-size: 0.78rem;
        font-weight: 700;
        letter-spacing: 0.02em;
        color: #FFFFFF;
    }}

    /* Bigger, more futuristic search box */
    div[data-baseweb="select"] > div {{
        min-height: 3.3rem;
        border-radius: 14px !important;
        border: 1.5px solid #D3DEE6 !important;
        font-size: 1.08rem;
        background-color: #FBFDFF;
        transition: border-color 0.2s ease, box-shadow 0.2s ease;
    }}
    div[data-baseweb="select"]:focus-within > div {{
        border-color: #0067B1 !important;
        box-shadow: 0 0 0 4px rgba(0, 103, 177, 0.15), 0 0 22px rgba(0, 194, 255, 0.3);
    }}

    .stTabs [data-baseweb="tab-list"] {{ gap: 0.5rem; }}
    .stTabs [data-baseweb="tab"] {{
        border-radius: 8px 8px 0 0;
        font-weight: 600;
        padding: 0.6rem 1.2rem;
    }}
    </style>
    <div class="mc-topbar">{i18n.t(lang, "topbar")}</div>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------------- scoring ---

def compute_matches(selected: list, diseases: dict) -> list:
    selected_set = set(selected)
    results = []
    for name, info in diseases.items():
        disease_symptoms = set(info["symptoms"])
        matched = selected_set & disease_symptoms
        if not matched:
            continue
        recall = len(matched) / len(disease_symptoms)
        precision = len(matched) / len(selected_set)
        score = recall * 0.7 + precision * 0.3
        results.append(
            {
                "name": name,
                "info": info,
                "matched": sorted(matched),
                "missing": sorted(disease_symptoms - matched),
                "score": score,
            }
        )
    results.sort(key=lambda r: r["score"], reverse=True)
    return results


# ------------------------------------------------------------------ header ---

st.markdown(
    f'<div class="mc-breadcrumb">{i18n.t(lang, "breadcrumb")}</div>',
    unsafe_allow_html=True,
)
st.title(i18n.t(lang, "topbar"))
st.caption(i18n.t(lang, "app_caption"))

# ------------------------------------------------------------------ sidebar ---

st.sidebar.header(i18n.t(lang, "sidebar_filters_header"))
st.sidebar.caption(i18n.t(lang, "sidebar_filters_caption"))
category_labels = i18n.CATEGORY_LABELS.get(lang, i18n.CATEGORY_LABELS["en"])
categories = st.sidebar.multiselect(
    i18n.t(lang, "sidebar_categories_label"),
    options=["Physical", "Mental"],
    default=["Physical", "Mental"],
    format_func=lambda c: category_labels.get(c, c),
)

if not categories:
    st.sidebar.info(i18n.t(lang, "sidebar_select_category_warning"))

filtered_diseases = {
    name: info for name, info in DISEASES.items() if info["category"] in categories
}

st.sidebar.header(i18n.t(lang, "sidebar_about_header"))
st.sidebar.markdown(
    i18n.t(
        lang,
        "sidebar_about_text",
        total=len(DISEASES),
        physical=sum(1 for d in DISEASES.values() if d["category"] == "Physical"),
        mental=sum(1 for d in DISEASES.values() if d["category"] == "Mental"),
    )
)

# --------------------------------------------------------------------- tabs ---

tab_kids, tab_checker, tab_assistant, tab_mental_health, tab_upload, tab_hospital = st.tabs(
    [
        i18n.t(lang, "tab_kids"),
        i18n.t(lang, "tab_checker"),
        i18n.t(lang, "tab_assistant"),
        i18n.t(lang, "tab_mental_health"),
        i18n.t(lang, "tab_upload"),
        i18n.t(lang, "tab_hospital"),
    ]
)

# =========================================================== Tab 1: Kids ===

with tab_kids:
    st.subheader(i18n.t(lang, "kids_subheader"))
    st.caption(i18n.t(lang, "kids_caption"))
    if show_translation_note:
        st.info(i18n.t(lang, "translation_fallback_note"))

    kids_questions_t = (bundle or {}).get("kids_questions", {})
    kids_themes_t = (bundle or {}).get("kids_themes", {})
    answer_options = [
        i18n.t(lang, "answer_not_really"),
        i18n.t(lang, "answer_sometimes"),
        i18n.t(lang, "answer_a_lot"),
    ]
    answer_scores = {option: score for score, option in enumerate(answer_options)}

    kids_answers = {}
    for q in KIDS_QUESTIONS:
        kids_answers[q["key"]] = st.radio(
            kids_questions_t.get(q["key"], q["prompt"]),
            answer_options,
            index=None,
            key=f"kids_{q['key']}",
            horizontal=True,
        )

    st.divider()
    st.markdown(i18n.t(lang, "kids_one_more_question"))
    safety_answer = st.radio(
        kids_questions_t.get("safety", SAFETY_QUESTION["prompt"]),
        answer_options,
        index=None,
        key="kids_safety",
        horizontal=True,
    )

    check_in = st.button(i18n.t(lang, "kids_submit_button"), type="primary", key="kids_submit")

    if safety_answer in (answer_options[1], answer_options[2]):
        st.error(i18n.t(lang, "kids_safety_alert_title"), icon="💙")
        st.markdown(i18n.t(lang, "kids_safety_alert_body"))
        st.markdown(f"- {i18n.t(lang, 'kids_988_line')}")
        st.markdown(f"- {i18n.t(lang, 'kids_crisis_text_line')}")
        st.divider()

    if check_in or "kids_results_shown" in st.session_state:
        if check_in:
            st.session_state["kids_results_shown"] = True

        answered = {k: v for k, v in kids_answers.items() if v is not None}
        flagged_themes = [k for k, v in answered.items() if answer_scores.get(v, 0) >= 1]

        st.markdown(i18n.t(lang, "kids_what_we_noticed"))
        if not answered:
            st.info(i18n.t(lang, "kids_answer_prompt"))
        elif not flagged_themes:
            st.success(i18n.t(lang, "kids_steady"))
        else:
            for key in flagged_themes:
                theme = KIDS_THEMES[key]
                theme_t = kids_themes_t.get(key, {})
                with st.container(border=True):
                    st.markdown(f"##### {theme_t.get('title', theme['title'])}")
                    st.write(theme_t.get("blurb", theme["blurb"]))
                    st.markdown(f"💡 {theme_t.get('tip', theme['tip'])}")
                    st.caption(
                        f"{i18n.t(lang, 'kids_learn_more')}: "
                        f"[{theme['resource_label']}]({theme['resource_url']})"
                    )

        st.divider()
        st.markdown(i18n.t(lang, "kids_resources_header"))
        resource_details = i18n.KIDS_RESOURCE_DETAILS_I18N.get(lang, i18n.KIDS_RESOURCE_DETAILS_I18N["en"])
        for (label, _detail, url), localized_detail in zip(KIDS_RESOURCES, resource_details):
            st.markdown(f"- **[{label}]({url})**: {localized_detail}")

        st.caption(i18n.t(lang, "kids_footer_note"))

# ==================================================== Tab 2: Symptom Checker ===

with tab_checker:
    with st.expander(i18n.t(lang, "checker_disclaimer_title"), expanded=False):
        st.warning(i18n.t(lang, "checker_disclaimer_body"))
    if show_translation_note:
        st.info(i18n.t(lang, "translation_fallback_note"))

    st.subheader(i18n.t(lang, "checker_step1"))

    localized_filtered_diseases = localize_diseases(filtered_diseases) if filtered_diseases else {}
    symptom_pool = localized_symptom_pool(localized_filtered_diseases) if localized_filtered_diseases else []

    selected_symptoms = st.multiselect(
        i18n.t(lang, "checker_multiselect_label"),
        options=symptom_pool,
        placeholder=i18n.t(lang, "checker_multiselect_placeholder"),
    )

    analyze = st.button(i18n.t(lang, "checker_analyze_button"), type="primary", disabled=not selected_symptoms)

    emergency_label_to_canonical = {translate_symptom(canon): canon for canon in EMERGENCY_SYMPTOMS}
    localized_emergency_messages = i18n.EMERGENCY_MESSAGES_I18N.get(lang, i18n.EMERGENCY_MESSAGES_I18N["en"])
    active_emergencies = [
        emergency_label_to_canonical[s] for s in selected_symptoms if s in emergency_label_to_canonical
    ]
    if active_emergencies:
        st.error(i18n.t(lang, "checker_emergency_title"), icon="🚨")
        for canon in active_emergencies:
            st.error(localized_emergency_messages.get(canon, EMERGENCY_SYMPTOMS[canon]))
        st.markdown(i18n.t(lang, "checker_emergency_seek_help"))
        for label, detail in i18n.CRISIS_RESOURCES_I18N.get(lang, i18n.CRISIS_RESOURCES_I18N["en"]):
            st.markdown(f"- **{label}**: {detail}")
        st.divider()

    st.subheader(i18n.t(lang, "checker_step2"))

    if not selected_symptoms:
        st.info(i18n.t(lang, "checker_select_prompt"))
    elif analyze or "last_results" in st.session_state:
        if analyze:
            st.session_state["last_results"] = compute_matches(selected_symptoms, localized_filtered_diseases)
        results = st.session_state["last_results"]

        if not results:
            st.warning(i18n.t(lang, "checker_no_matches"))
        else:
            urgency_labels = i18n.URGENCY_LABELS_I18N.get(lang, i18n.URGENCY_LABELS_I18N["en"])
            top_results = results[:6]
            for r in top_results:
                info = r["info"]
                urgency_text = urgency_labels.get(info["urgency"], "")
                with st.container(border=True):
                    col1, col2 = st.columns([3, 1])
                    with col1:
                        st.markdown(f"#### {info.get('display_name', r['name'])}")
                        st.caption(i18n.t(lang, "checker_category_label", category=category_labels.get(info["category"], info["category"])))
                    with col2:
                        badge_color = BADGE_COLORS.get(info["urgency"], "#5B6B79")
                        st.markdown(
                            f'<span class="mc-badge" style="background-color:{badge_color};">{urgency_text}</span>',
                            unsafe_allow_html=True,
                        )

                    st.progress(min(r["score"], 1.0), text=i18n.t(lang, "checker_match_score", pct=f"{r['score']*100:.0f}"))

                    st.write(info["description"])
                    st.markdown(i18n.t(lang, "checker_matched_symptoms", symptoms=", ".join(r["matched"])))
                    if r["missing"]:
                        st.markdown(i18n.t(lang, "checker_missing_symptoms", symptoms=", ".join(r["missing"])))
                    st.markdown(i18n.t(lang, "checker_suggested_next_step", advice=info["advice"]))
                    if info.get("mayo_summary"):
                        with st.expander(i18n.t(lang, "checker_mayo_expander")):
                            st.write(info["mayo_summary"])
                            if info.get("mayo_url"):
                                st.caption(i18n.t(lang, "checker_mayo_source", url=info["mayo_url"]))

            st.divider()
            st.caption(i18n.t(lang, "checker_footer_note"))

# ===================================================== Tab 3: AI Assistant ===

with tab_assistant:
    st.subheader(i18n.t(lang, "assistant_subheader"))
    st.caption(i18n.t(lang, "assistant_caption"))

    if not rag.is_configured():
        st.warning(i18n.t(lang, "assistant_not_configured"))
    else:
        with st.spinner(i18n.t(lang, "assistant_preparing_kb")):
            rag.ensure_default_knowledge_base_seeded()

        if "assistant_history" not in st.session_state:
            st.session_state.assistant_history = []

        for message in st.session_state.assistant_history:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        question = st.chat_input(i18n.t(lang, "assistant_chat_placeholder"))
        if question:
            st.session_state.assistant_history.append({"role": "user", "content": question})
            with st.chat_message("user"):
                st.markdown(question)

            with st.chat_message("assistant"):
                if rag.contains_crisis_language(question):
                    st.error(i18n.t(lang, "kids_safety_alert_title"), icon="💙")
                    for label, detail in i18n.CRISIS_RESOURCES_I18N.get(lang, i18n.CRISIS_RESOURCES_I18N["en"]):
                        st.markdown(f"- **{label}**: {detail}")
                    answer = i18n.t(lang, "assistant_crisis_answer")
                    st.markdown(answer)
                else:
                    try:
                        with st.spinner(i18n.t(lang, "assistant_thinking")):
                            try:
                                matches = rag.search_similar(question)
                            except Exception:
                                # Knowledge base search is best-effort; fall back to the
                                # model's own general knowledge if it fails.
                                matches = []
                            history = st.session_state.assistant_history[:-1]
                            answer = rag.generate_answer(
                                question, matches, history=history, language=i18n.LANGUAGES[lang]
                            )
                    except Exception as exc:
                        matches = []
                        answer = i18n.t(lang, "assistant_error_prefix", error=exc)
                    st.markdown(answer)
                    if matches:
                        sources = sorted({m["source"] for m in matches})
                        st.caption(i18n.t(lang, "assistant_sources_prefix", sources=", ".join(sources)))

            st.session_state.assistant_history.append({"role": "assistant", "content": answer})

# ================================================== Tab 4: Mental Health ===

with tab_mental_health:
    st.subheader(i18n.t(lang, "mh_subheader"))
    st.caption(i18n.t(lang, "mh_caption"))

    with st.expander(i18n.t(lang, "mh_disclaimer_title"), expanded=False):
        st.warning(i18n.t(lang, "mh_disclaimer_body"))
    if show_translation_note:
        st.info(i18n.t(lang, "translation_fallback_note"))

    mh_questions_t = (bundle or {}).get("mh_questions", {})
    mh_severity_labels_t = (bundle or {}).get("mh_severity_labels", {})

    st.markdown(f"**{i18n.t(lang, 'mh_depression_header')}**")
    depression_answers = {}
    for q in DEPRESSION_QUESTIONS:
        depression_answers[q["key"]] = st.radio(
            mh_questions_t.get(q["key"], q["prompt"]),
            MH_ANSWER_OPTIONS,
            index=None,
            key=f"mh_{q['key']}",
            horizontal=True,
        )

    st.divider()
    st.markdown(f"**{i18n.t(lang, 'mh_anxiety_header')}**")
    anxiety_answers = {}
    for q in ANXIETY_QUESTIONS:
        anxiety_answers[q["key"]] = st.radio(
            mh_questions_t.get(q["key"], q["prompt"]),
            MH_ANSWER_OPTIONS,
            index=None,
            key=f"mh_{q['key']}",
            horizontal=True,
        )

    st.divider()
    st.markdown(i18n.t(lang, "mh_one_more_question"))
    mh_safety_answer = st.radio(
        mh_questions_t.get("safety", MH_SAFETY_QUESTION["prompt"]),
        MH_ANSWER_OPTIONS,
        index=None,
        key="mh_safety",
        horizontal=True,
    )

    all_answered = (
        all(v is not None for v in depression_answers.values())
        and all(v is not None for v in anxiety_answers.values())
        and mh_safety_answer is not None
    )

    mh_submit = st.button(
        i18n.t(lang, "mh_submit_button"), type="primary", key="mh_submit", disabled=not all_answered
    )

    if mh_safety_answer in MH_ANSWER_OPTIONS[1:]:
        st.error(i18n.t(lang, "kids_safety_alert_title"), icon="💙")
        st.markdown(i18n.t(lang, "mh_safety_alert_body"))
        st.markdown(f"- {i18n.t(lang, 'kids_988_line')}")
        st.markdown(f"- {i18n.t(lang, 'kids_crisis_text_line')}")
        st.divider()

    if not all_answered:
        st.info(i18n.t(lang, "mh_prompt"))
    elif mh_submit or "mh_results_shown" in st.session_state:
        if mh_submit:
            st.session_state["mh_results_shown"] = True

        answer_scores = {opt: i for i, opt in enumerate(MH_ANSWER_OPTIONS)}
        dep_score = sum(answer_scores[v] for v in depression_answers.values()) + answer_scores[mh_safety_answer]
        anx_score = sum(answer_scores[v] for v in anxiety_answers.values())

        dep_label, dep_color = severity_band(dep_score, DEPRESSION_SEVERITY_BANDS)
        anx_label, anx_color = severity_band(anx_score, ANXIETY_SEVERITY_BANDS)

        def mh_label(label):
            return mh_severity_labels_t.get(label, label)

        st.markdown(i18n.t(lang, "mh_results_header"))
        with st.container(border=True):
            st.markdown(
                f":{dep_color}[{i18n.t(lang, 'mh_depression_result', label=mh_label(dep_label), score=dep_score)}]"
            )
            st.progress(min(dep_score / 27, 1.0))
            with st.expander(i18n.t(lang, "mh_learn_more_depression")):
                dep_info = localize_diseases(
                    {"Major Depressive Disorder": DISEASES["Major Depressive Disorder"]}
                )["Major Depressive Disorder"]
                st.write(dep_info["description"])
                if dep_info.get("mayo_summary"):
                    st.write(dep_info["mayo_summary"])
                st.caption(f"[Mayo Clinic]({dep_info['mayo_url']})")

        with st.container(border=True):
            st.markdown(
                f":{anx_color}[{i18n.t(lang, 'mh_anxiety_result', label=mh_label(anx_label), score=anx_score)}]"
            )
            st.progress(min(anx_score / 12, 1.0))
            with st.expander(i18n.t(lang, "mh_learn_more_anxiety")):
                anx_info = localize_diseases(
                    {"Generalized Anxiety Disorder": DISEASES["Generalized Anxiety Disorder"]}
                )["Generalized Anxiety Disorder"]
                st.write(anx_info["description"])
                if anx_info.get("mayo_summary"):
                    st.write(anx_info["mayo_summary"])
                st.caption(f"[Mayo Clinic]({anx_info['mayo_url']})")

        st.caption(i18n.t(lang, "mh_results_note"))

        st.divider()
        st.markdown(i18n.t(lang, "mh_resources_header"))
        resource_details = i18n.MENTAL_HEALTH_RESOURCE_DETAILS_I18N.get(
            lang, i18n.MENTAL_HEALTH_RESOURCE_DETAILS_I18N["en"]
        )
        for (label, _detail, url), localized_detail in zip(MENTAL_HEALTH_RESOURCES, resource_details):
            st.markdown(f"- **[{label}]({url})**: {localized_detail}")

    st.caption(i18n.t(lang, "mh_footer_note"))

# =================================================== Tab 5: Upload Documents ===

with tab_upload:
    st.subheader(i18n.t(lang, "upload_subheader"))
    st.caption(i18n.t(lang, "upload_caption"))

    if not rag.is_configured():
        st.warning(i18n.t(lang, "upload_not_configured"))
    else:
        stats = rag.store_stats()
        st.caption(i18n.t(lang, "upload_kb_stats", chunks=stats["chunks"], documents=stats["documents"]))

        admin_password = rag.get_secret("ADMIN_PASSWORD")
        if not admin_password:
            st.info(i18n.t(lang, "upload_set_password"))
        else:
            entered_password = st.text_input(
                i18n.t(lang, "upload_password_label"), type="password", key="admin_password_input"
            )
            if entered_password == admin_password:
                uploaded_files = st.file_uploader(
                    i18n.t(lang, "upload_file_uploader_label"),
                    type=["txt", "md", "pdf"],
                    accept_multiple_files=True,
                    key="doc_uploader",
                )
                if uploaded_files and st.button(i18n.t(lang, "upload_add_button"), key="add_docs"):
                    for uploaded_file in uploaded_files:
                        with st.spinner(i18n.t(lang, "upload_processing", filename=uploaded_file.name)):
                            try:
                                text = rag.extract_text(uploaded_file)
                                chunk_count = rag.upsert_document(uploaded_file.name, text)
                            except Exception as exc:
                                st.error(i18n.t(lang, "upload_error", filename=uploaded_file.name, error=exc))
                            else:
                                st.success(i18n.t(lang, "upload_success", filename=uploaded_file.name, count=chunk_count))
            elif entered_password:
                st.error(i18n.t(lang, "upload_incorrect_password"))

# ==================================================== Tab 6: Find a Hospital ===

with tab_hospital:
    st.subheader(i18n.t(lang, "hospital_subheader"))
    st.caption(i18n.t(lang, "hospital_caption"))

    col1, col2 = st.columns([1, 2])
    with col1:
        use_location = st.button(i18n.t(lang, "hospital_use_location_button"), type="primary")
    with col2:
        manual_location = st.text_input(
            i18n.t(lang, "hospital_manual_location_label"),
            placeholder=i18n.t(lang, "hospital_manual_location_placeholder"),
        )
        manual_search = st.button(i18n.t(lang, "hospital_search_button"))

    radius_km = st.slider(i18n.t(lang, "hospital_radius_label"), min_value=2, max_value=50, value=10, step=1)

    origin = None
    origin_label = None

    if use_location:
        attempt = st.session_state.get("geo_attempt", 0) + 1
        st.session_state["geo_attempt"] = attempt
        with st.spinner(i18n.t(lang, "hospital_getting_location")):
            location = get_geolocation(component_key=f"geo_{attempt}")

        if location and location.get("coords"):
            origin = (location["coords"]["latitude"], location["coords"]["longitude"])
            origin_label = i18n.t(lang, "hospital_your_location_label")
        elif location and location.get("error"):
            st.error(i18n.t(lang, "hospital_geo_error", error=location["error"]["message"]))

    if manual_search and manual_location:
        geocode_failed = False
        with st.spinner(i18n.t(lang, "hospital_looking_up")):
            try:
                geocoded = hospital_finder.geocode_location(manual_location)
            except Exception:
                geocoded = None
                geocode_failed = True
                st.error(i18n.t(lang, "hospital_geocode_service_error"))
        if geocoded is not None:
            lat, lon, display_name = geocoded
            origin = (lat, lon)
            origin_label = display_name
        elif not geocode_failed:
            st.warning(i18n.t(lang, "hospital_not_found"))

    if origin is not None:
        lat, lon = origin
        st.session_state["hospital_origin"] = (lat, lon, origin_label)
        with st.spinner(i18n.t(lang, "hospital_searching")):
            try:
                st.session_state["hospital_results"] = hospital_finder.find_nearby_hospitals(
                    lat, lon, radius_km=radius_km
                )
            except Exception:
                st.session_state["hospital_results"] = []
                st.error(i18n.t(lang, "hospital_search_service_error"))

    if "hospital_origin" in st.session_state:
        lat, lon, display_name = st.session_state["hospital_origin"]
        hospitals = st.session_state.get("hospital_results", [])
        st.caption(i18n.t(lang, "hospital_showing_results", location=display_name))

        if not hospitals:
            st.info(i18n.t(lang, "hospital_no_results"))
        else:
            map_points = [{"lat": lat, "lon": lon, "color": "#0067B1", "size": 120}]
            map_points += [
                {"lat": h["lat"], "lon": h["lon"], "color": "#C8102E", "size": 80} for h in hospitals
            ]
            st.map(map_points, latitude="lat", longitude="lon", color="color", size="size")

            for h in hospitals:
                with st.container(border=True):
                    col_a, col_b = st.columns([3, 1])
                    with col_a:
                        st.markdown(f"#### {h['name']}")
                        if h["address"]:
                            st.caption(h["address"])
                    with col_b:
                        st.markdown(i18n.t(lang, "hospital_distance_away", distance=f"{h['distance_km']:.1f}"))
                    if h["emergency"]:
                        st.markdown(i18n.t(lang, "hospital_has_er"))
                    if h["phone"]:
                        st.markdown(f"📞 {h['phone']}")
                    st.markdown(i18n.t(lang, "hospital_get_directions", url=h["directions_url"]))
    else:
        st.info(i18n.t(lang, "hospital_prompt"))

st.divider()
st.caption(i18n.t(lang, "footer"))
