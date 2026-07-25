import streamlit as st

from quiz_data import (
    QUESTIONS,
    CATEGORIES,
    SCALE_LABELS,
    SAFETY_QUESTION,
    CRISIS_RESOURCES,
    score_answers,
)

st.set_page_config(
    page_title="Mental Health Check-In Quiz",
    page_icon="🧠",
    layout="wide",
)

st.title("🧠 Mental Health Check-In Quiz")
st.caption(
    "A short, informal self-reflection quiz about how you've been feeling over "
    "the **past two weeks**. It is **not** a diagnosis or a clinical screening tool."
)

with st.expander("⚠️ Important disclaimer — please read", expanded=False):
    st.warning(
        "This quiz is for **educational and self-reflection purposes only**. It is "
        "not a medical device, a diagnosis, or a substitute for professional advice. "
        "Results are based on a simple, non-clinical scoring model. If you are "
        "struggling, please reach out to a qualified mental health professional. "
        "If you are in crisis or thinking about harming yourself, contact emergency "
        "services or a crisis line immediately."
    )

st.divider()

with st.form("mental_health_quiz"):
    st.subheader("1. A few questions about the last two weeks")
    st.caption("For each statement, choose how often it applied to you.")

    answers = {}
    for category in CATEGORIES:
        st.markdown(f"**{category}**")
        for q in [q for q in QUESTIONS if q["category"] == category]:
            answers[q["id"]] = st.radio(
                q["text"],
                options=SCALE_LABELS,
                index=None,
                horizontal=True,
                key=q["id"],
            )
        st.write("")

    st.markdown("**One more thing**")
    safety_answer = st.radio(
        SAFETY_QUESTION["text"],
        options=["No", "Yes"],
        index=None,
        horizontal=True,
        key=SAFETY_QUESTION["id"],
    )

    submitted = st.form_submit_button("See my results", type="primary")

if submitted:
    unanswered = [q["text"] for q in QUESTIONS if answers[q["id"]] is None]
    if safety_answer is None:
        unanswered.append(SAFETY_QUESTION["text"])

    if unanswered:
        st.error("Please answer every question before seeing your results.")
    else:
        st.session_state["quiz_results"] = score_answers(answers)
        st.session_state["quiz_safety_flag"] = safety_answer == "Yes"

st.divider()
st.subheader("2. Your results")

if "quiz_results" not in st.session_state:
    st.info("Answer the questions above and click **See my results**.")
else:
    if st.session_state.get("quiz_safety_flag"):
        st.error("### 🚨 Please reach out for support", icon="🚨")
        st.error(
            "You indicated you've had thoughts of harming yourself or that you'd be "
            "better off not being here. You deserve support, and you don't have to "
            "go through this alone."
        )
        st.markdown("**Crisis and emergency resources:**")
        for label, detail in CRISIS_RESOURCES:
            st.markdown(f"- **{label}**: {detail}")
        st.divider()

    results = st.session_state["quiz_results"]

    st.markdown(f"### Overall: :{results['band_color']}[{results['band_label']}]")
    st.progress(
        min(results["total"] / results["max_total"], 1.0),
        text=f"Score: {results['total']} / {results['max_total']}",
    )
    st.write(results["band_message"])

    st.markdown("#### Breakdown by area")
    cols = st.columns(len(CATEGORIES))
    for col, category in zip(cols, CATEGORIES):
        cat_total = results["category_totals"][category]
        cat_max = results["category_max"][category]
        with col:
            st.caption(category)
            st.progress(min(cat_total / cat_max, 1.0) if cat_max else 0.0)
            st.caption(f"{cat_total} / {cat_max}")

    st.divider()
    st.caption(
        "This quiz reflects general themes based on your answers, not a diagnosis. "
        "Please consult a licensed mental health professional to discuss how you've "
        "been feeling."
    )

st.divider()
st.caption(
    "Built for educational/hackathon purposes. Always consult a licensed medical "
    "or mental health professional for real diagnosis and treatment."
)
