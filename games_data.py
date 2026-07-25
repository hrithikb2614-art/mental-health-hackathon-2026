"""Content for the Games & Breathing Exercises tab: lightweight, non-clinical
interactive tools for stress relief, grounding, and relaxation. These are
coping aids, not therapy or treatment.
"""

# (inhale, hold, exhale, hold) seconds per phase. A "0" phase is skipped.
BREATHING_PATTERNS = {
    "box": {"inhale": 4, "hold1": 4, "exhale": 4, "hold2": 4},
    "relaxing": {"inhale": 4, "hold1": 7, "exhale": 8, "hold2": 0},
    "belly": {"inhale": 4, "hold1": 0, "exhale": 6, "hold2": 0},
}
BREATHING_PATTERN_ORDER = ["box", "relaxing", "belly"]

# (key, count, emoji) for the classic 5-4-3-2-1 grounding technique.
GROUNDING_STEPS = [
    ("see", 5, "👀"),
    ("touch", 4, "✋"),
    ("hear", 3, "👂"),
    ("smell", 2, "👃"),
    ("taste", 1, "👅"),
]

BUBBLE_COUNT = 24

# Canonical English affirmations. Index-aligned with AFFIRMATIONS_I18N in i18n.py.
AFFIRMATIONS = [
    "This feeling is temporary, and it will pass.",
    "I am doing the best I can with what I have right now.",
    "It's okay to rest. Rest is productive too.",
    "I don't have to have it all figured out today.",
    "I am allowed to take up space and ask for help.",
    "Small steps still count as progress.",
    "I've gotten through hard days before, and I can get through this one.",
    "My feelings are valid, even when they're hard to explain.",
    "I am not my thoughts. I can notice them without believing every one.",
    "Being kind to myself is not selfish. It's necessary.",
]
