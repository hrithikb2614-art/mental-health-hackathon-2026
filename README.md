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

The app has four tabs:

1. **Kids & Teens Check-In** — a supportive, non-diagnostic self-reflection
   survey for young people. Surfaces gentle themes instead of condition
   labels and always shows curated resources (NAMI, MHA National, NIMH,
   SAMHSA, 988, Crisis Text Line).
2. **Symptom Checker** — covers 30+ conditions across physical illness
   (cold, flu, COVID-19, migraine, UTI, diabetes, etc.) and mental health
   (depression, anxiety, PTSD, OCD, bipolar disorder, ADHD, etc.), with a
   multi-select symptom picker, ranked matches with a match-score bar,
   matched/missing symptoms, suggested next steps, an AI-generated Mayo
   Clinic summary per condition, and an automatic safety banner with crisis
   hotline info if emergency symptoms are selected.
3. **AI Assistant** — a RAG-powered chat that answers questions grounded in
   documents loaded into a local knowledge base (see setup below). Falls
   back to a clear setup message if not configured.
4. **Upload Documents** — a password-gated page to add `.txt`, `.md`, or
   `.pdf` files to the shared knowledge base the AI Assistant searches.

## Running locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

The Kids Check-In and Symptom Checker tabs work with no further setup. The
AI Assistant and Upload Documents tabs need the setup below.

## AI Assistant setup (optional)

The AI Assistant stores document embeddings in a local file
(`data/knowledge_base.json`, gitignored) — no external database or account
needed. It uses OpenAI for embeddings and chat answers.

1. Copy `.streamlit/secrets.toml.example` to `.streamlit/secrets.toml`
   (already gitignored) and fill in:
   - `OPENAI_API_KEY` — an OpenAI API key
   - `ADMIN_PASSWORD` — a password of your choosing; required to use the
     Upload Documents tab, since uploaded documents are shared with every
     visitor's AI Assistant
2. Restart the app. Use the password-gated Upload Documents tab to add
   `.txt`, `.md`, or `.pdf` files to the knowledge base, then ask questions
   in the AI Assistant tab.

Without `OPENAI_API_KEY` configured, the AI Assistant and Upload Documents
tabs show a setup message and the rest of the app works normally. Note that
the knowledge base lives on local disk, so it persists only for the
lifetime of the running app process — redeploying resets it.

## How it works

Each condition in `health_data.py` has a list of typical symptoms. When you
select your symptoms, the app scores every condition by how much its symptom
list overlaps with your selection (weighted toward recall — how much of the
condition's typical profile you match) and shows the top matches.
