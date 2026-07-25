import streamlit as st

from health_data import (
    DISEASES,
    EMERGENCY_SYMPTOMS,
    CRISIS_RESOURCES,
    URGENCY_LABELS,
    build_symptom_pool,
)

st.set_page_config(
    page_title="Symptom Checker — Physical & Mental Health",
    page_icon="🩺",
    layout="wide",
)

# Visual style inspired by mayoclinic.org/diseases-conditions: navy/blue palette,
# clean sans-serif type, top bar + breadcrumb, pill-style badges.
BADGE_COLORS = {
    "emergency": "#C8102E",
    "see_doctor": "#0067B1",
    "self_care": "#2E7D32",
}

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Roboto', -apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif;
    }

    .mc-topbar {
        background-color: #0B2D4D;
        color: #FFFFFF;
        margin: -1rem -1rem 0 -1rem;
        padding: 0.85rem 1.5rem;
        border-bottom: 4px solid #0067B1;
        font-size: 1rem;
        font-weight: 600;
        letter-spacing: 0.03em;
        text-transform: uppercase;
    }
    .mc-breadcrumb {
        margin: 0.75rem 0 0.25rem 0;
        color: #5B6B79;
        font-size: 0.85rem;
    }

    h1, h2, h3 { color: #0B2D4D !important; font-weight: 700 !important; }
    a, a:visited { color: #0067B1; }

    .stButton > button {
        background-color: #0067B1;
        color: #FFFFFF;
        border: none;
        border-radius: 4px;
        font-weight: 600;
        padding: 0.5rem 1.4rem;
    }
    .stButton > button:hover { background-color: #00517F; color: #FFFFFF; }
    .stButton > button:disabled { background-color: #C7D3DB; color: #FFFFFF; }

    section[data-testid="stSidebar"] {
        background-color: #F4F6F8;
        border-right: 1px solid #E1E5E9;
    }

    div[data-testid="stVerticalBlockBorderWrapper"] {
        border-radius: 6px !important;
        border: 1px solid #E1E5E9 !important;
        box-shadow: 0 1px 3px rgba(11, 45, 77, 0.06);
    }

    .stProgress > div > div > div > div { background-color: #0067B1; }

    .mc-badge {
        display: inline-block;
        padding: 4px 12px;
        border-radius: 999px;
        font-size: 0.78rem;
        font-weight: 700;
        letter-spacing: 0.02em;
        color: #FFFFFF;
    }
    </style>
    <div class="mc-topbar">🩺 Symptom Checker</div>
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
    '<div class="mc-breadcrumb">Home &nbsp;›&nbsp; Diseases &amp; Conditions &nbsp;›&nbsp; Symptom Checker</div>',
    unsafe_allow_html=True,
)
st.title("🩺 Symptom Checker — Physical & Mental Health")
st.caption(
    "A rule-based tool that suggests possible conditions from symptom overlap. "
    "It is **not** a diagnosis."
)

with st.expander("⚠️ Important disclaimer — please read", expanded=False):
    st.warning(
        "This tool is for **educational purposes only** and does not provide medical "
        "or mental health advice, diagnosis, or treatment. It uses simple symptom "
        "matching, not a clinical or AI model. Always consult a qualified doctor or "
        "mental health professional for any health concern. If you believe you are "
        "having a medical or mental health emergency, contact your local emergency "
        "services immediately."
    )

# ------------------------------------------------------------------ sidebar ---

st.sidebar.header("Filters")
categories = st.sidebar.multiselect(
    "Which areas do you want to check?",
    options=["Physical", "Mental"],
    default=["Physical", "Mental"],
)

if not categories:
    st.sidebar.info("Select at least one category to continue.")

filtered_diseases = {
    name: info for name, info in DISEASES.items() if info["category"] in categories
}

st.sidebar.header("About")
st.sidebar.markdown(
    "This checker cross-references the symptoms you select against a curated "
    f"list of **{len(DISEASES)} conditions** ({sum(1 for d in DISEASES.values() if d['category']=='Physical')} physical, "
    f"{sum(1 for d in DISEASES.values() if d['category']=='Mental')} mental health) "
    "and ranks them by how closely your symptoms match each condition's typical profile."
)

# ------------------------------------------------------------------- input ---

st.subheader("1. Select your symptoms")

symptom_pool = build_symptom_pool(filtered_diseases) if filtered_diseases else []

selected_symptoms = st.multiselect(
    "Start typing to search, or scroll to browse. Select as many as apply.",
    options=symptom_pool,
    placeholder="e.g. persistent sadness, headache, shortness of breath...",
)

analyze = st.button("Analyze symptoms", type="primary", disabled=not selected_symptoms)

# --------------------------------------------------------------- emergency ---

active_emergencies = [s for s in selected_symptoms if s in EMERGENCY_SYMPTOMS]
if active_emergencies:
    st.error("### 🚨 This may be a medical emergency", icon="🚨")
    for s in active_emergencies:
        st.error(EMERGENCY_SYMPTOMS[s])
    st.markdown("**Please seek immediate help. Crisis and emergency resources:**")
    for label, detail in CRISIS_RESOURCES:
        st.markdown(f"- **{label}**: {detail}")
    st.divider()

# -------------------------------------------------------------- results -----

st.subheader("2. Possible matches")

if not selected_symptoms:
    st.info("Select one or more symptoms above, then click **Analyze symptoms**.")
elif analyze or "last_results" in st.session_state:
    if analyze:
        st.session_state["last_results"] = compute_matches(selected_symptoms, filtered_diseases)
    results = st.session_state["last_results"]

    if not results:
        st.warning("No matching conditions found for the selected symptoms in this reference set.")
    else:
        top_results = results[:6]
        for r in top_results:
            info = r["info"]
            urgency_text, _ = URGENCY_LABELS.get(info["urgency"], ("", "gray"))
            with st.container(border=True):
                col1, col2 = st.columns([3, 1])
                with col1:
                    st.markdown(f"#### {r['name']}")
                    st.caption(f"Category: {info['category']}")
                with col2:
                    badge_color = BADGE_COLORS.get(info["urgency"], "#5B6B79")
                    st.markdown(
                        f'<span class="mc-badge" style="background-color:{badge_color};">{urgency_text}</span>',
                        unsafe_allow_html=True,
                    )

                st.progress(min(r["score"], 1.0), text=f"Match score: {r['score']*100:.0f}%")

                st.write(info["description"])
                st.markdown(f"✅ **Matched symptoms:** {', '.join(r['matched'])}")
                if r["missing"]:
                    st.markdown(f"ℹ️ **Other typical symptoms not selected:** {', '.join(r['missing'])}")
                st.markdown(f"**Suggested next step:** {info['advice']}")
                if info.get("mayo_summary"):
                    with st.expander("📖 AI summary from Mayo Clinic"):
                        st.write(info["mayo_summary"])
                        if info.get("mayo_url"):
                            st.caption(f"Source: [Mayo Clinic]({info['mayo_url']})")

        st.divider()
        st.caption(
            "Results are ranked by symptom overlap only and may include conditions "
            "that are not relevant to you. This is not a diagnosis — please consult "
            "a healthcare professional to confirm any condition."
        )

st.divider()
st.caption(
    "Built for educational/hackathon purposes. Always consult a licensed medical "
    "or mental health professional for real diagnosis and treatment."
)
