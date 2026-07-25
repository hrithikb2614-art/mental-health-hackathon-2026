import streamlit as st

from health_data import (
    DISEASES,
    EMERGENCY_SYMPTOMS,
    CRISIS_RESOURCES,
    URGENCY_LABELS,
    build_symptom_pool,
)
from kids_data import (
    ANSWER_OPTIONS,
    ANSWER_SCORES,
    KIDS_QUESTIONS,
    SAFETY_QUESTION,
    KIDS_THEMES,
    KIDS_RESOURCES,
)
import hospital_finder

st.set_page_config(
    page_title="Symptom Checker — Physical & Mental Health",
    page_icon="🩺",
    layout="wide",
)

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
    <div class="mc-topbar">🩺&nbsp; Symptom &amp; Wellness Checker</div>
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
    '<div class="mc-breadcrumb">Home &nbsp;›&nbsp; Diseases &amp; Conditions &nbsp;›&nbsp; Symptom &amp; Wellness Checker</div>',
    unsafe_allow_html=True,
)
st.title("🩺 Symptom & Wellness Checker")
st.caption(
    "A friendly check-in for kids & teens, plus a rule-based symptom-overlap tool for "
    "physical and mental health. Neither is a diagnosis."
)

# ------------------------------------------------------------------ sidebar ---

st.sidebar.header("Filters")
st.sidebar.caption("Applies to the Symptom Checker tab.")
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

# --------------------------------------------------------------------- tabs ---

tab_kids, tab_checker, tab_hospital = st.tabs(
    [
        "🧒 Kids & Teens Check-In",
        "🔍 Symptom Checker",
        "🏥 Find a Hospital",
    ]
)

# =========================================================== Tab 1: Kids ===

with tab_kids:
    st.subheader("A quick, friendly check-in")
    st.caption(
        "This isn't a test, a score, or a diagnosis — just a few questions to help you notice "
        "how you've been feeling lately. Answer honestly. Nothing here is judged, and your "
        "answers aren't saved anywhere."
    )

    kids_answers = {}
    for q in KIDS_QUESTIONS:
        kids_answers[q["key"]] = st.radio(
            q["prompt"],
            ANSWER_OPTIONS,
            index=None,
            key=f"kids_{q['key']}",
            horizontal=True,
        )

    st.divider()
    st.markdown(
        "**One more question.** This one's just about keeping you safe — it's always okay "
        "to answer honestly."
    )
    safety_answer = st.radio(
        SAFETY_QUESTION["prompt"],
        ANSWER_OPTIONS,
        index=None,
        key="kids_safety",
        horizontal=True,
    )

    check_in = st.button("See what this might mean", type="primary", key="kids_submit")

    if safety_answer in ("Sometimes", "A lot"):
        st.error("💙 Your safety matters most right now", icon="💙")
        st.markdown(
            "Thank you for being honest — that takes courage. Please tell a trusted adult "
            "right away (a parent, relative, teacher, or school counselor), or reach out now:"
        )
        st.markdown("- **[988 Suicide & Crisis Lifeline](https://988lifeline.org/)**: Call or text 988 — free, confidential, 24/7.")
        st.markdown("- **[Crisis Text Line](https://www.crisistextline.org/)**: Text HOME to 741741 — free, 24/7.")
        st.divider()

    if check_in or "kids_results_shown" in st.session_state:
        if check_in:
            st.session_state["kids_results_shown"] = True

        answered = {k: v for k, v in kids_answers.items() if v is not None}
        flagged_themes = [k for k, v in answered.items() if ANSWER_SCORES.get(v, 0) >= 1]

        st.markdown("#### What we noticed")
        if not answered:
            st.info("Answer a few questions above to see your check-in summary.")
        elif not flagged_themes:
            st.success(
                "Based on your answers, things sound fairly steady right now. That's great — "
                "and it's always okay to check in with someone you trust if that changes."
            )
        else:
            for key in flagged_themes:
                theme = KIDS_THEMES[key]
                with st.container(border=True):
                    st.markdown(f"##### {theme['title']}")
                    st.write(theme["blurb"])
                    st.markdown(f"💡 {theme['tip']}")
                    st.caption(f"Learn more: [{theme['resource_label']}]({theme['resource_url']})")

        st.divider()
        st.markdown("#### Resources for you")
        for label, detail, url in KIDS_RESOURCES:
            st.markdown(f"- **[{label}]({url})**: {detail}")

        st.caption(
            "This check-in is not a diagnosis and doesn't replace talking to a real person. "
            "A parent, relative, teacher, school counselor, or doctor can help you figure out "
            "what to do next."
        )

# ==================================================== Tab 2: Symptom Checker ===

with tab_checker:
    with st.expander("⚠️ Important disclaimer — please read", expanded=False):
        st.warning(
            "This tool is for **educational purposes only** and does not provide medical "
            "or mental health advice, diagnosis, or treatment. It uses simple symptom "
            "matching, not a clinical or AI model. Always consult a qualified doctor or "
            "mental health professional for any health concern. If you believe you are "
            "having a medical or mental health emergency, contact your local emergency "
            "services immediately."
        )

    st.subheader("1. Select your symptoms")

    symptom_pool = build_symptom_pool(filtered_diseases) if filtered_diseases else []

    selected_symptoms = st.multiselect(
        "Start typing to search, or scroll to browse. Select as many as apply.",
        options=symptom_pool,
        placeholder="🔍  e.g. persistent sadness, headache, shortness of breath...",
    )

    analyze = st.button("Analyze symptoms", type="primary", disabled=not selected_symptoms)

    active_emergencies = [s for s in selected_symptoms if s in EMERGENCY_SYMPTOMS]
    if active_emergencies:
        st.error("### 🚨 This may be a medical emergency", icon="🚨")
        for s in active_emergencies:
            st.error(EMERGENCY_SYMPTOMS[s])
        st.markdown("**Please seek immediate help. Crisis and emergency resources:**")
        for label, detail in CRISIS_RESOURCES:
            st.markdown(f"- **{label}**: {detail}")
        st.divider()

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

# ==================================================== Tab 3: Find a Hospital ===

with tab_hospital:
    st.subheader("Find a nearby hospital")
    st.caption(
        "Enter a city, address, or zip code to see nearby hospitals on a map, using free "
        "OpenStreetMap data — no account or API key needed. **If this is a real emergency, "
        "call your local emergency number (e.g. 911/112/999) instead of waiting on this page.**"
    )

    location_query = st.text_input(
        "Your location",
        placeholder="e.g. Boston, MA  or  10001  or  221B Baker Street, London",
    )
    radius_km = st.slider("Search radius (km)", min_value=2, max_value=50, value=10, step=1)
    search = st.button("Find hospitals", type="primary", disabled=not location_query)

    if search:
        geocode_failed = False
        with st.spinner("Locating you..."):
            try:
                geocoded = hospital_finder.geocode_location(location_query)
            except Exception:
                geocoded = None
                geocode_failed = True
                st.error(
                    "Couldn't reach the location service. Check your internet connection "
                    "and try again."
                )

        if geocoded is None:
            st.session_state.pop("hospital_origin", None)
            st.session_state.pop("hospital_results", None)
            if not geocode_failed:
                st.warning("Couldn't find that location. Try a more specific address or city.")
        else:
            lat, lon, display_name = geocoded
            st.session_state["hospital_origin"] = (lat, lon, display_name)
            with st.spinner("Searching for nearby hospitals..."):
                try:
                    st.session_state["hospital_results"] = hospital_finder.find_nearby_hospitals(
                        lat, lon, radius_km=radius_km
                    )
                except Exception:
                    st.session_state["hospital_results"] = []
                    st.error(
                        "Couldn't reach the hospital search service. Check your internet "
                        "connection and try again."
                    )

    if "hospital_origin" in st.session_state:
        lat, lon, display_name = st.session_state["hospital_origin"]
        hospitals = st.session_state.get("hospital_results", [])
        st.caption(f"📍 Showing results near **{display_name}**")

        if not hospitals:
            st.info("No hospitals found in this radius. Try increasing the search radius.")
        else:
            map_points = [{"lat": lat, "lon": lon, "color": "#0067B1", "size": 120}]
            map_points += [
                {"lat": h["lat"], "lon": h["lon"], "color": "#C8102E", "size": 80} for h in hospitals
            ]
            st.map(map_points, latitude="lat", longitude="lon", color="color", size="size")

            for h in hospitals:
                with st.container(border=True):
                    col1, col2 = st.columns([3, 1])
                    with col1:
                        st.markdown(f"#### {h['name']}")
                        if h["address"]:
                            st.caption(h["address"])
                    with col2:
                        st.markdown(f"**{h['distance_km']:.1f} km away**")
                    if h["emergency"]:
                        st.markdown("🚨 **Has an emergency department**")
                    if h["phone"]:
                        st.markdown(f"📞 {h['phone']}")
                    st.markdown(f"[Get directions ↗]({h['directions_url']})")

st.divider()
st.caption(
    "Built for educational/hackathon purposes. Always consult a licensed medical "
    "or mental health professional for real diagnosis and treatment."
)
