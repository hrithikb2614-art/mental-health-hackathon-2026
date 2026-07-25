"""Question bank and scoring logic for the mental health check-in quiz.

This is an original, informal self-reflection quiz (not a clinical or
diagnostic instrument such as PHQ-9/GAD-7). It is for educational purposes
only. Scoring is a simple weighted sum used to surface general, non-clinical
themes worth reflecting on — not a diagnosis.
"""

# Likert-style answer scale shared by every scored question.
SCALE = [
    ("Never", 0),
    ("Occasionally", 1),
    ("Frequently", 2),
    ("Almost constantly", 3),
]
SCALE_LABELS = [label for label, _ in SCALE]
SCALE_SCORES = dict(SCALE)

QUESTIONS = [
    {"id": "q1", "category": "Mood", "text": "I have felt down, sad, or hopeless."},
    {"id": "q2", "category": "Mood", "text": "I have lost interest or pleasure in things I used to enjoy."},
    {"id": "q3", "category": "Anxiety", "text": "I have felt nervous, anxious, or on edge."},
    {"id": "q4", "category": "Anxiety", "text": "I have found it hard to stop or control worrying."},
    {"id": "q5", "category": "Stress", "text": "I have felt overwhelmed by everyday responsibilities."},
    {"id": "q6", "category": "Stress", "text": "I have felt irritable or easily frustrated."},
    {"id": "q7", "category": "Sleep & Energy", "text": "I have had trouble falling asleep, staying asleep, or sleeping too much."},
    {"id": "q8", "category": "Sleep & Energy", "text": "I have felt tired or low on energy during the day."},
    {"id": "q9", "category": "Social Connection", "text": "I have felt isolated or disconnected from people I care about."},
    {"id": "q10", "category": "Social Connection", "text": "I have avoided spending time with others."},
    {"id": "q11", "category": "Focus & Motivation", "text": "I have had trouble concentrating on everyday tasks."},
    {"id": "q12", "category": "Focus & Motivation", "text": "I have struggled to find motivation to do things I need to do."},
]

CATEGORIES = list(dict.fromkeys(q["category"] for q in QUESTIONS))
MAX_SCORE_PER_QUESTION = max(score for _, score in SCALE)
MAX_TOTAL_SCORE = len(QUESTIONS) * MAX_SCORE_PER_QUESTION

# Asked on its own, outside the scored scale, so a "yes" always surfaces
# crisis resources regardless of the overall score.
SAFETY_QUESTION = {
    "id": "safety",
    "text": "Have you recently had thoughts of harming yourself, or that you'd be better off not being here?",
}

RESULT_BANDS = [
    (0, 8, "Low signs of distress", "green",
     "Your answers suggest you're doing relatively well right now. Keep up habits "
     "that support your wellbeing, and reach out for support if things change."),
    (9, 17, "Mild signs of distress", "blue",
     "Your answers suggest some mild signs of stress or low mood. Self-care, rest, "
     "and talking to someone you trust can help. Consider checking in with a "
     "counselor if this continues."),
    (18, 26, "Moderate signs of distress", "orange",
     "Your answers suggest a moderate level of distress. It may help to speak with "
     "a mental health professional about what you've been experiencing."),
    (27, MAX_TOTAL_SCORE, "High signs of distress", "red",
     "Your answers suggest a significant level of distress. Please consider reaching "
     "out to a mental health professional soon, and lean on your support network."),
]

CRISIS_RESOURCES = [
    ("US — 988 Suicide & Crisis Lifeline", "Call or text 988 (24/7)"),
    ("US — Crisis Text Line", "Text HOME to 741741"),
    ("International Association for Suicide Prevention", "https://www.iasp.info/resources/Crisis_Centres/"),
    ("Emergency services", "If you are in immediate danger, call your local emergency number (e.g., 911/112/999)."),
]


def score_answers(answers: dict) -> dict:
    """Score quiz answers.

    answers: {question_id: answer_label} for each question in QUESTIONS.
    Returns total score, per-category scores, and the matching result band.
    """
    total = 0
    category_totals = {c: 0 for c in CATEGORIES}
    category_max = {c: 0 for c in CATEGORIES}

    for q in QUESTIONS:
        value = SCALE_SCORES[answers[q["id"]]]
        total += value
        category_totals[q["category"]] += value
        category_max[q["category"]] += MAX_SCORE_PER_QUESTION

    band = next(
        (b for b in RESULT_BANDS if b[0] <= total <= b[1]),
        RESULT_BANDS[-1],
    )

    return {
        "total": total,
        "max_total": MAX_TOTAL_SCORE,
        "category_totals": category_totals,
        "category_max": category_max,
        "band_label": band[2],
        "band_color": band[3],
        "band_message": band[4],
    }
