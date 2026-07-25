# Symptom Checker — Physical & Mental Health

A Streamlit app that helps users explore possible physical and mental health
conditions based on selected symptoms, using a curated rule-based symptom
overlap model (no external APIs or ML training required). It also includes a
short, informal Mental Health Check-In Quiz.

## ⚠️ Disclaimer

This tool is for **educational purposes only**. It is not a medical device
and does not provide diagnosis or treatment. Always consult a qualified
doctor or mental health professional. If you are experiencing a medical or
mental health emergency, contact your local emergency services immediately.

## Features

- Covers 30+ conditions across physical illness (cold, flu, COVID-19,
  migraine, UTI, diabetes, etc.) and mental health (depression, anxiety,
  PTSD, OCD, bipolar disorder, ADHD, etc.)
- Multi-select symptom picker with search
- Ranked matches with a match-score bar, matched/missing symptoms, and
  suggested next steps (self-care / see a doctor / emergency)
- Automatic safety banner with crisis hotline info if emergency symptoms
  (e.g. thoughts of self-harm, chest pain) are selected
- Filter by Physical, Mental, or both
- **Mental Health Check-In Quiz** (`pages/1_🧠_Mental_Health_Quiz.py`): a short,
  informal 12-question self-reflection quiz covering mood, anxiety, stress,
  sleep/energy, social connection, and focus/motivation. Gives an overall and
  per-area score with a plain-language summary, plus a dedicated safety
  question that immediately surfaces crisis resources if answered "Yes".

## Running locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

Use the sidebar page navigator to switch to the **Mental Health Quiz** page.

## How it works

Each condition in `health_data.py` has a list of typical symptoms. When you
select your symptoms, the app scores every condition by how much its symptom
list overlaps with your selection (weighted toward recall — how much of the
condition's typical profile you match) and shows the top matches.
