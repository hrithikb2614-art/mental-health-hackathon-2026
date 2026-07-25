"""Content for the adult Mental Health Check-In tab.

A supportive, non-diagnostic self-reflection questionnaire inspired by
widely used, publicly available clinical screening instruments (the PHQ-9
for depression, the GAD-7 for anxiety), paraphrased here for a general
wellness check-in. This is NOT a diagnostic tool, does not replace a full
clinical evaluation, and does not label anyone with a condition.
"""

ANSWER_OPTIONS = ["Not at all", "Several days", "More than half the days", "Nearly every day"]

DEPRESSION_QUESTIONS = [
    {"key": "interest", "prompt": "Little interest or pleasure in doing things"},
    {"key": "down", "prompt": "Feeling down, depressed, or hopeless"},
    {"key": "sleep", "prompt": "Trouble falling or staying asleep, or sleeping too much"},
    {"key": "energy", "prompt": "Feeling tired or having little energy"},
    {"key": "appetite", "prompt": "Poor appetite or overeating"},
    {"key": "self_worth", "prompt": "Feeling bad about yourself, or that you're a failure, or have let yourself or your family down"},
    {"key": "concentration", "prompt": "Trouble concentrating on things, such as reading or watching TV"},
    {"key": "psychomotor", "prompt": "Moving or speaking so slowly that others could have noticed — or the opposite, being fidgety or restless"},
]

SAFETY_QUESTION = {
    "key": "safety",
    "prompt": "Thoughts that you would be better off dead, or of hurting yourself in some way",
}

ANXIETY_QUESTIONS = [
    {"key": "nervous", "prompt": "Feeling nervous, anxious, or on edge"},
    {"key": "worry_control", "prompt": "Not being able to stop or control worrying"},
    {"key": "relax", "prompt": "Trouble relaxing"},
    {"key": "afraid", "prompt": "Feeling afraid, as if something awful might happen"},
]

# (low, high, label, color) — standard PHQ-9 interpretation bands (0-27, 9
# items scored 0-3), applied here to depression_score = 8 questions + safety.
DEPRESSION_SEVERITY_BANDS = [
    (0, 4, "Minimal", "green"),
    (5, 9, "Mild", "blue"),
    (10, 14, "Moderate", "orange"),
    (15, 19, "Moderately severe", "orange"),
    (20, 27, "Severe", "red"),
]

# Proportional bands for a 4-item, 0-3 anxiety check (max 12).
ANXIETY_SEVERITY_BANDS = [
    (0, 3, "Minimal", "green"),
    (4, 6, "Mild", "blue"),
    (7, 9, "Moderate", "orange"),
    (10, 12, "Severe", "red"),
]

# (label, detail, url) — always shown alongside the results.
MENTAL_HEALTH_RESOURCES = [
    (
        "988 Suicide & Crisis Lifeline",
        "Call or text 988 — free, confidential, 24/7.",
        "https://988lifeline.org/",
    ),
    (
        "Crisis Text Line",
        "Text HOME to 741741 — free, 24/7 support by text.",
        "https://www.crisistextline.org/",
    ),
    (
        "NAMI HelpLine",
        "Call 1-800-950-6264 or text \"HelpLine\" to 62640. Mon-Fri, 10am-10pm ET. Free peer support and referrals — not a crisis line (use 988 for a crisis).",
        "https://www.nami.org/help",
    ),
    (
        "SAMHSA National Helpline",
        "Call 1-800-662-HELP (4357), 24/7/365, free and confidential, English & Spanish. Treatment referrals for mental health and substance use.",
        "https://www.samhsa.gov/find-help/helplines/national-helpline",
    ),
]


def severity_band(score: int, bands: list):
    """Return (label, color) for the band containing score, clamping to the last band."""
    for low, high, label, color in bands:
        if low <= score <= high:
            return label, color
    return bands[-1][2], bands[-1][3]
