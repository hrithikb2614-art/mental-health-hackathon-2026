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
            urgency_text, urgency_color = URGENCY_LABELS.get(info["urgency"], ("", "gray"))
            with st.container(border=True):
                col1, col2 = st.columns([3, 1])
                with col1:
                    st.markdown(f"#### {r['name']}")
                    st.caption(f"Category: {info['category']}")
                with col2:
                    st.markdown(f":{urgency_color}[**{urgency_text}**]")

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
