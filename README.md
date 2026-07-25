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
   geolocation) or type a city/address/zip, and see a live Google Map
   centered there with nearby hospitals as pins. Needs a Google Maps API
   key (see setup below).

## Running locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

The Kids Check-In and Symptom Checker tabs work with no further setup. The
Find a Hospital tab needs the Google Maps setup below.

## Find a Hospital setup

The map is powered by Google's Maps Embed API, and "Use my location" uses
your browser's built-in geolocation — neither needs any account of yours
beyond a Google Cloud API key.

1. In [Google Cloud Console](https://console.cloud.google.com/), create a
   project (or reuse one), enable the **Maps Embed API**, and create an API
   key. Restrict the key (HTTP referrers) to the domain(s) you deploy this
   app to — Maps API keys are used client-side and are visible in the page,
   so restriction is what keeps them safe, not secrecy.
2. Copy `.streamlit/secrets.toml.example` to `.streamlit/secrets.toml`
   (already gitignored) and set:
   - `GOOGLE_MAPS_API_KEY` — the API key from step 1
3. Restart the app.

The Maps Embed API itself is free with no query limit, but the Cloud
project still needs billing enabled to issue API keys. Without
`GOOGLE_MAPS_API_KEY` configured, the Find a Hospital tab shows a setup
message and the rest of the app works normally.

Browser geolocation requires a secure context (HTTPS, or `localhost` during
local development) and the user granting permission when prompted.

## How it works

Each condition in `health_data.py` has a list of typical symptoms. When you
select your symptoms, the app scores every condition by how much its symptom
list overlaps with your selection (weighted toward recall — how much of the
condition's typical profile you match) and shows the top matches.
