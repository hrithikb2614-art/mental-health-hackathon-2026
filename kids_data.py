"""Content for the Kids & Teens Check-In tab.

This is a supportive self-reflection check-in for young people (roughly
ages 8-17) — NOT a diagnostic tool or clinical screener. It never labels a
child with a condition; it surfaces gentle, validating themes and points to
real resources, and always encourages talking to a trusted adult.

Content is informed by (paraphrased, not copied, with attribution/links):
- NAMI (National Alliance on Mental Illness) — nami.org
- Mental Health America (MHA) — mhanational.org
- NIMH (National Institute of Mental Health) — nimh.nih.gov
- SAMHSA (Substance Abuse and Mental Health Services Administration) — samhsa.gov
"""

ANSWER_OPTIONS = ["Not really", "Sometimes", "A lot"]
ANSWER_SCORES = {"Not really": 0, "Sometimes": 1, "A lot": 2}

KIDS_QUESTIONS = [
    {
        "key": "mood",
        "prompt": "Have you been feeling sad, down, or like things aren't fun anymore?",
    },
    {
        "key": "worry",
        "prompt": "Have you been feeling worried or nervous, even about small things?",
    },
    {
        "key": "sleep",
        "prompt": "Has your sleep been off lately (trouble falling asleep, staying asleep, or sleeping a lot more or less than usual)?",
    },
    {
        "key": "focus",
        "prompt": "Has it been hard to focus, sit still, or finish things at school or at home?",
    },
    {
        "key": "social",
        "prompt": "Have you been wanting to be alone a lot and pulling away from friends or family?",
    },
    {
        "key": "body_image",
        "prompt": "Have you been worrying a lot about food, eating, or how your body looks?",
    },
]

SAFETY_QUESTION = {
    "key": "safety",
    "prompt": "Have you had thoughts of hurting yourself, or thoughts that you don't want to be here anymore?",
}

KIDS_THEMES = {
    "mood": {
        "title": "Feeling sad or low",
        "blurb": (
            "It sounds like sadness or low energy has been showing up a lot. Everyone feels "
            "down sometimes, but when it sticks around and takes the fun out of things you used "
            "to enjoy, it's worth talking about — not something to just push through alone."
        ),
        "tip": "Try naming the feeling out loud to someone you trust — a parent, relative, teacher, or school counselor.",
        "resource_label": "NIMH — Child & Adolescent Mental Health",
        "resource_url": "https://www.nimh.nih.gov/health/topics/child-and-adolescent-mental-health",
    },
    "worry": {
        "title": "Worry and nervous feelings",
        "blurb": (
            "It sounds like worry has been feeling heavy. Some worry is normal, but when it's "
            "hard to shake or shows up about lots of things, that's a real feeling worth sharing "
            "with someone who can help you carry it."
        ),
        "tip": "Notice what tends to trigger the worry — it can help a trusted adult understand what's going on.",
        "resource_label": "MHA — Youth Mental Health Resources",
        "resource_url": "https://mhanational.org/youth-mental-health/",
    },
    "sleep": {
        "title": "Sleep changes",
        "blurb": (
            "Sleep and mood are closely connected, so changes in how you're sleeping — too little, "
            "too much, or trouble settling down — are a meaningful signal, not just an inconvenience."
        ),
        "tip": "A consistent bedtime and less screen time before bed can help, but if it keeps happening, tell a trusted adult.",
        "resource_label": "NIMH — Child & Adolescent Mental Health",
        "resource_url": "https://www.nimh.nih.gov/health/topics/child-and-adolescent-mental-health",
    },
    "focus": {
        "title": "Trouble focusing or sitting still",
        "blurb": (
            "Having a hard time focusing, staying organized, or sitting still can be frustrating — "
            "and it isn't about not trying hard enough. It's worth mentioning to a parent or "
            "teacher so you can get support that actually helps."
        ),
        "tip": "Breaking tasks into small steps and taking movement breaks can help in the moment.",
        "resource_label": "MHA — Youth Mental Health Test",
        "resource_url": "https://screening.mhanational.org/screening-tools/youth/",
    },
    "social": {
        "title": "Pulling away from others",
        "blurb": (
            "Wanting space sometimes is normal, but pulling away from friends and family a lot, "
            "or losing interest in spending time with people you used to enjoy being around, is "
            "something to gently talk about with someone you trust."
        ),
        "tip": "You don't have to explain everything at once — even saying \"I've been feeling off\" is a good start.",
        "resource_label": "NAMI — Teen & Young Adult HelpLine",
        "resource_url": "https://www.nami.org/nami-helpline/teen-young-adult-helpline/",
    },
    "body_image": {
        "title": "Worry about food or body image",
        "blurb": (
            "Spending a lot of time worrying about eating, weight, or how your body looks can be "
            "exhausting, and it's more common than it feels. This is something a doctor, counselor, "
            "or trusted adult can genuinely help with."
        ),
        "tip": "You deserve support without judgment — a school counselor or doctor is a safe place to start.",
        "resource_label": "MHA — Youth Mental Health Resources",
        "resource_url": "https://mhanational.org/youth-mental-health/",
    },
}

# Always-shown resources for the Kids & Teens Check-In tab.
KIDS_RESOURCES = [
    (
        "988 Suicide & Crisis Lifeline",
        "Call or text 988 — free, confidential, 24/7. For any crisis, not just suicide.",
        "https://988lifeline.org/",
    ),
    (
        "Crisis Text Line",
        "Text HOME to 741741 — free, 24/7 support by text.",
        "https://www.crisistextline.org/",
    ),
    (
        "NAMI Teen & Young Adult HelpLine",
        "Call 1-800-950-6264, text \"Friend\" to 62640, or chat at nami.org/talktous. Mon–Fri, 10am–10pm ET. Free peer support — not a crisis line (use 988 for a crisis).",
        "https://www.nami.org/nami-helpline/teen-young-adult-helpline/",
    ),
    (
        "SAMHSA National Helpline",
        "Call 1-800-662-HELP (4357), 24/7/365, free and confidential, English & Spanish. Treatment referrals for mental health and substance use.",
        "https://www.samhsa.gov/find-help/helplines/national-helpline",
    ),
    (
        "MHA Youth Mental Health Test",
        "A free, anonymous screening tool for ages 11-17 to check in on emotions, attention, or behavior.",
        "https://screening.mhanational.org/screening-tools/youth/",
    ),
    (
        "NIMH — Child & Adolescent Mental Health",
        "Clear, research-based information for kids, teens, and families.",
        "https://www.nimh.nih.gov/health/topics/child-and-adolescent-mental-health",
    ),
]
