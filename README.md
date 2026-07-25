# Symptom Checker — Physical & Mental Health

A Streamlit app that helps users explore possible physical and mental health
conditions based on selected symptoms, using a curated rule-based symptom
overlap model (no external APIs or ML training required).

## ⚠️ Disclaimer

This tool is for **educational purposes only**. It is not a medical device
and does not provide diagnosis or treatment. Always consult a qualified
doctor or mental health professional. If you are experiencing a medical or
mental health emergency, contact your local emergency services immediately.

## Features

The app has three tabs:

1. **Kids & Teens Check-In** — a supportive, non-diagnostic self-reflection
   survey for young people. Surfaces gentle themes instead of condition
   labels and always shows curated resources (NAMI, MHA National, NIMH,
   SAMHSA, 988, Crisis Text Line).
2. **Symptom Checker** — covers 30+ conditions across physical illness
   (cold, flu, COVID-19, migraine, UTI, diabetes, etc.) and mental health
   (depression, anxiety, PTSD, OCD, bipolar disorder, ADHD, etc.), with a
   multi-select symptom picker, ranked matches with a match-score bar,
   matched/missing symptoms, suggested next steps, a Mayo Clinic summary per
   condition, and an automatic safety banner with crisis hotline info if
   emergency symptoms are selected.
3. **Find a Hospital** — click "Use my location" (uses your browser's
   geolocation) or type a city/address/zip, and see nearby hospitals on a
   free map with a distance-sorted list (address, phone, one-tap
   directions). Uses OpenStreetMap's free Nominatim (geocoding) and
   Overpass (place search) APIs — no API key or account needed.

## Running locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

No API keys or setup are required — every tab works out of the box, as
long as the machine running it has normal internet access (needed only by
the Find a Hospital tab, to reach OpenStreetMap). Browser geolocation for
"Use my location" requires a secure context (HTTPS, or `localhost` during
local development) and the user granting permission when prompted.

## How it works

Each condition in `health_data.py` has a list of typical symptoms. When you
select your symptoms, the app scores every condition by how much its symptom
list overlaps with your selection (weighted toward recall — how much of the
condition's typical profile you match) and shows the top matches.
