"""Symptom Checker — Physical & Mental Health (single-file version).

A rule-based Streamlit app that suggests possible physical and mental
health conditions from selected symptoms. Not a diagnosis — for
educational purposes only.

Run with:
    pip install streamlit
    streamlit run single_app.py
"""

import streamlit as st

# =============================================================================
# Data: curated symptom -> condition reference (not a trained model)
# =============================================================================

DISEASES = {
    # ---------------- Physical health ----------------
    "Common Cold": {
        "category": "Physical",
        "symptoms": ["runny nose", "sneezing", "sore throat", "mild cough", "congestion", "mild fatigue", "mild headache"],
        "description": "A mild viral infection of the upper respiratory tract.",
        "urgency": "self_care",
        "advice": "Rest, fluids, and over-the-counter remedies usually help. See a doctor if symptoms last over 10 days or worsen.",
    },
    "Influenza (Flu)": {
        "category": "Physical",
        "symptoms": ["high fever", "chills", "body aches", "fatigue", "dry cough", "headache", "sore throat", "congestion"],
        "description": "A contagious viral infection that is often more severe than a cold.",
        "urgency": "see_doctor",
        "advice": "Rest and hydrate; antivirals can help if started early. Seek care if breathing becomes difficult.",
    },
    "COVID-19": {
        "category": "Physical",
        "symptoms": ["fever", "dry cough", "fatigue", "loss of taste or smell", "shortness of breath", "sore throat", "body aches", "headache"],
        "description": "A viral respiratory illness caused by the SARS-CoV-2 virus.",
        "urgency": "see_doctor",
        "advice": "Test if possible, isolate, and monitor oxygen levels. Seek emergency care for severe breathing trouble.",
    },
    "Migraine": {
        "category": "Physical",
        "symptoms": ["throbbing headache", "nausea", "sensitivity to light", "sensitivity to sound", "visual disturbances", "dizziness"],
        "description": "A neurological condition causing intense, recurring headaches.",
        "urgency": "self_care",
        "advice": "Rest in a dark quiet room; consider a doctor if attacks are frequent or severe.",
    },
    "Tension Headache": {
        "category": "Physical",
        "symptoms": ["dull headache", "neck stiffness", "scalp tenderness", "mild fatigue", "difficulty concentrating"],
        "description": "The most common type of headache, often linked to stress or muscle tension.",
        "urgency": "self_care",
        "advice": "Rest, hydration, and stress management usually resolve it. See a doctor if frequent.",
    },
    "Gastroenteritis": {
        "category": "Physical",
        "symptoms": ["nausea", "vomiting", "diarrhea", "abdominal cramps", "mild fever", "fatigue"],
        "description": "Inflammation of the stomach and intestines, often from infection.",
        "urgency": "see_doctor",
        "advice": "Stay hydrated with fluids/electrolytes. Seek care if unable to keep fluids down or signs of dehydration appear.",
    },
    "Food Poisoning": {
        "category": "Physical",
        "symptoms": ["nausea", "vomiting", "diarrhea", "abdominal cramps", "sudden onset after eating", "weakness"],
        "description": "Illness caused by consuming contaminated food.",
        "urgency": "see_doctor",
        "advice": "Hydrate and rest. Seek care if symptoms are severe or persist beyond 2 days.",
    },
    "Urinary Tract Infection": {
        "category": "Physical",
        "symptoms": ["burning urination", "frequent urination", "pelvic pain", "cloudy urine", "urgency to urinate", "mild fever"],
        "description": "A bacterial infection affecting the urinary system.",
        "urgency": "see_doctor",
        "advice": "See a doctor for antibiotics; drink plenty of water in the meantime.",
    },
    "Allergic Rhinitis": {
        "category": "Physical",
        "symptoms": ["sneezing", "itchy eyes", "runny nose", "congestion", "watery eyes", "itchy throat"],
        "description": "An allergic reaction causing cold-like symptoms, often seasonal.",
        "urgency": "self_care",
        "advice": "Antihistamines and avoiding triggers often help. See a doctor for persistent symptoms.",
    },
    "Asthma": {
        "category": "Physical",
        "symptoms": ["shortness of breath", "wheezing", "chest tightness", "cough", "difficulty breathing"],
        "description": "A chronic condition causing narrowing and inflammation of the airways.",
        "urgency": "see_doctor",
        "advice": "Use prescribed inhalers as directed. Seek emergency care for severe breathing difficulty.",
    },
    "Hypertension": {
        "category": "Physical",
        "symptoms": ["headache", "dizziness", "blurred vision", "shortness of breath", "nosebleeds", "no obvious symptoms"],
        "description": "Persistently high blood pressure, often with few noticeable symptoms.",
        "urgency": "see_doctor",
        "advice": "Get blood pressure checked regularly; lifestyle changes and medication can help manage it.",
    },
    "Type 2 Diabetes": {
        "category": "Physical",
        "symptoms": ["excessive thirst", "frequent urination", "fatigue", "blurred vision", "slow healing wounds", "unexplained weight loss"],
        "description": "A chronic condition affecting how the body processes blood sugar.",
        "urgency": "see_doctor",
        "advice": "See a doctor for blood sugar testing; diet, exercise, and medication can help manage it.",
    },
    "GERD (Acid Reflux)": {
        "category": "Physical",
        "symptoms": ["heartburn", "regurgitation", "chest discomfort", "sour taste", "difficulty swallowing", "bloating"],
        "description": "A digestive condition where stomach acid frequently flows back into the esophagus.",
        "urgency": "self_care",
        "advice": "Avoid trigger foods and eating late. See a doctor if symptoms persist or worsen.",
    },
    "Iron-Deficiency Anemia": {
        "category": "Physical",
        "symptoms": ["fatigue", "pale skin", "weakness", "shortness of breath", "dizziness", "cold hands and feet"],
        "description": "A condition caused by insufficient healthy red blood cells due to low iron.",
        "urgency": "see_doctor",
        "advice": "See a doctor for blood tests; iron supplementation may be recommended.",
    },
    "Hypothyroidism": {
        "category": "Physical",
        "symptoms": ["fatigue", "weight gain", "cold intolerance", "dry skin", "constipation", "depressed mood", "hair loss"],
        "description": "A condition where the thyroid gland doesn't produce enough hormones.",
        "urgency": "see_doctor",
        "advice": "See a doctor for thyroid function tests; treatment is usually straightforward with medication.",
    },
    "Dehydration": {
        "category": "Physical",
        "symptoms": ["thirst", "dry mouth", "fatigue", "dizziness", "dark urine", "headache"],
        "description": "A condition caused by losing more fluids than you take in.",
        "urgency": "self_care",
        "advice": "Increase fluid intake. Seek care if severe or unable to keep fluids down.",
    },
    "Sinusitis": {
        "category": "Physical",
        "symptoms": ["facial pain", "nasal congestion", "thick nasal discharge", "reduced smell", "headache", "cough"],
        "description": "Inflammation of the sinuses, often following a cold.",
        "urgency": "self_care",
        "advice": "Saline rinses and decongestants can help. See a doctor if symptoms last over 10 days.",
    },
    "Strep Throat": {
        "category": "Physical",
        "symptoms": ["severe sore throat", "difficulty swallowing", "fever", "swollen tonsils", "swollen neck glands", "no cough"],
        "description": "A bacterial throat infection that needs antibiotic treatment.",
        "urgency": "see_doctor",
        "advice": "See a doctor for testing and antibiotics if confirmed.",
    },
    "Conjunctivitis (Pink Eye)": {
        "category": "Physical",
        "symptoms": ["red eyes", "itchy eyes", "watery eyes", "eye discharge", "gritty feeling in eye"],
        "description": "Inflammation or infection of the membrane covering the eye.",
        "urgency": "self_care",
        "advice": "Keep eyes clean and avoid touching them. See a doctor if it worsens or vision is affected.",
    },
    "Muscle/Back Strain": {
        "category": "Physical",
        "symptoms": ["back pain", "muscle stiffness", "pain with movement", "muscle spasm", "localized soreness"],
        "description": "An injury to muscles or tendons, often from overuse or improper lifting.",
        "urgency": "self_care",
        "advice": "Rest, ice/heat, and gentle stretching help. See a doctor if pain is severe or persistent.",
    },

    # ---------------- Mental health ----------------
    "Major Depressive Disorder": {
        "category": "Mental",
        "symptoms": ["persistent sadness", "loss of interest", "fatigue", "sleep changes", "appetite changes", "difficulty concentrating", "feelings of worthlessness", "thoughts of death"],
        "description": "A mood disorder causing persistent feelings of sadness and loss of interest.",
        "urgency": "see_doctor",
        "advice": "Speak with a mental health professional. Therapy and/or medication are effective treatments.",
    },
    "Generalized Anxiety Disorder": {
        "category": "Mental",
        "symptoms": ["excessive worry", "restlessness", "muscle tension", "fatigue", "difficulty concentrating", "irritability", "sleep changes"],
        "description": "A condition marked by chronic, excessive worry about everyday matters.",
        "urgency": "see_doctor",
        "advice": "Therapy (like CBT), relaxation techniques, and sometimes medication can help significantly.",
    },
    "Panic Disorder": {
        "category": "Mental",
        "symptoms": ["sudden intense fear", "racing heart", "chest tightness", "shortness of breath", "trembling", "fear of losing control", "dizziness"],
        "description": "Recurrent, unexpected panic attacks and fear of future attacks.",
        "urgency": "see_doctor",
        "advice": "A mental health professional can help with therapy and coping strategies; treatment is very effective.",
    },
    "Social Anxiety Disorder": {
        "category": "Mental",
        "symptoms": ["fear of social situations", "fear of judgment", "avoidance of social events", "racing heart in social settings", "excessive self-consciousness", "blushing"],
        "description": "Intense fear or anxiety about being watched or judged by others.",
        "urgency": "see_doctor",
        "advice": "Cognitive behavioral therapy is highly effective; consider speaking with a therapist.",
    },
    "Post-Traumatic Stress Disorder": {
        "category": "Mental",
        "symptoms": ["intrusive memories", "flashbacks", "nightmares", "avoidance of reminders", "hypervigilance", "irritability", "emotional numbness"],
        "description": "A condition triggered by experiencing or witnessing a traumatic event.",
        "urgency": "see_doctor",
        "advice": "Trauma-focused therapy is effective. Reach out to a mental health professional.",
    },
    "Obsessive-Compulsive Disorder": {
        "category": "Mental",
        "symptoms": ["intrusive thoughts", "repetitive behaviors", "need for symmetry", "excessive checking", "excessive cleaning", "distress from unwanted thoughts"],
        "description": "A condition featuring unwanted repetitive thoughts and/or behaviors.",
        "urgency": "see_doctor",
        "advice": "Specialized therapy (ERP) and/or medication are effective; consult a mental health professional.",
    },
    "Bipolar Disorder": {
        "category": "Mental",
        "symptoms": ["mood swings", "elevated mood", "decreased need for sleep", "impulsivity", "racing thoughts", "persistent sadness", "fatigue"],
        "description": "A condition causing extreme mood shifts including emotional highs and lows.",
        "urgency": "see_doctor",
        "advice": "See a psychiatrist for evaluation; mood stabilizers and therapy are commonly used.",
    },
    "Insomnia Disorder": {
        "category": "Mental",
        "symptoms": ["difficulty falling asleep", "difficulty staying asleep", "waking up too early", "daytime fatigue", "irritability", "difficulty concentrating"],
        "description": "A sleep disorder marked by persistent trouble sleeping.",
        "urgency": "self_care",
        "advice": "Improve sleep hygiene; see a doctor if it persists beyond a few weeks.",
    },
    "ADHD (Attention-Deficit/Hyperactivity Disorder)": {
        "category": "Mental",
        "symptoms": ["difficulty concentrating", "impulsivity", "restlessness", "forgetfulness", "disorganization", "trouble finishing tasks"],
        "description": "A neurodevelopmental condition affecting attention, impulse control, and activity levels.",
        "urgency": "see_doctor",
        "advice": "An evaluation from a specialist can clarify diagnosis; behavioral strategies and/or medication can help.",
    },
    "Burnout / Chronic Stress": {
        "category": "Mental",
        "symptoms": ["emotional exhaustion", "cynicism", "reduced performance", "fatigue", "irritability", "sleep changes", "difficulty concentrating"],
        "description": "A state of physical and emotional exhaustion caused by prolonged stress.",
        "urgency": "self_care",
        "advice": "Rest, boundary-setting, and support help; consider a professional if it doesn't improve.",
    },
    "Eating Disorder (Disordered Eating)": {
        "category": "Mental",
        "symptoms": ["preoccupation with food or weight", "restrictive eating", "binge eating", "purging behaviors", "distorted body image", "fatigue"],
        "description": "A condition involving unhealthy patterns of eating that affect physical and mental health.",
        "urgency": "see_doctor",
        "advice": "Reach out to a doctor or specialist; early support greatly improves outcomes.",
    },
    "Adjustment Disorder": {
        "category": "Mental",
        "symptoms": ["low mood after stressful event", "anxiety after stressful event", "trouble adjusting to change", "sleep changes", "difficulty concentrating"],
        "description": "Emotional or behavioral symptoms in response to an identifiable stressor.",
        "urgency": "self_care",
        "advice": "Support from friends, family, or a counselor can help you adjust; seek help if symptoms persist.",
    },
}

# Symptoms that should always trigger an immediate safety banner, regardless
# of the overall disease ranking. Each maps to a short, direct message.
EMERGENCY_SYMPTOMS = {
    "thoughts of death": "You mentioned thoughts of death or self-harm.",
    "thoughts of self-harm or suicide": "You mentioned thoughts of self-harm or suicide.",
    "chest pain": "Chest pain can be a sign of a medical emergency.",
    "severe difficulty breathing": "Severe difficulty breathing needs immediate attention.",
    "sudden numbness or weakness on one side": "This can be a sign of a stroke.",
    "loss of consciousness": "Loss of consciousness needs immediate medical attention.",
    "severe uncontrolled bleeding": "Severe bleeding needs immediate medical attention.",
}

CRISIS_RESOURCES = [
    ("US — 988 Suicide & Crisis Lifeline", "Call or text 988 (24/7)"),
    ("US — Crisis Text Line", "Text HOME to 741741"),
    ("International Association for Suicide Prevention", "https://www.iasp.info/resources/Crisis_Centres/"),
    ("Emergency services", "If you are in immediate danger, call your local emergency number (e.g., 911/112/999)."),
]

URGENCY_LABELS = {
    "emergency": ("🚨 Seek immediate care", "red"),
    "see_doctor": ("🩺 See a doctor", "orange"),
    "self_care": ("🏠 Usually self-care", "green"),
}


def build_symptom_pool(diseases: dict) -> list:
    """Return a sorted, de-duplicated list of every symptom + emergency flag."""
    pool = set()
    for info in diseases.values():
        pool.update(info["symptoms"])
    pool.update(EMERGENCY_SYMPTOMS.keys())
    return sorted(pool)


# =============================================================================
# Scoring
# =============================================================================

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


# =============================================================================
# UI
# =============================================================================

st.set_page_config(
    page_title="Symptom Checker — Physical & Mental Health",
    page_icon="🩺",
    layout="wide",
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

st.subheader("1. Select your symptoms")

symptom_pool = build_symptom_pool(filtered_diseases) if filtered_diseases else []

selected_symptoms = st.multiselect(
    "Start typing to search, or scroll to browse. Select as many as apply.",
    options=symptom_pool,
    placeholder="e.g. persistent sadness, headache, shortness of breath...",
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
