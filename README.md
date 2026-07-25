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

The app has seven tabs, and a sidebar language picker (English, Spanish,
French, Hindi — see [Languages](#languages) below):

1. **Kids & Teens Check-In** — a supportive, non-diagnostic self-reflection
   survey for young people. Surfaces gentle themes instead of condition
   labels and always shows curated resources (NAMI, MHA National, NIMH,
   SAMHSA, 988, Crisis Text Line).
2. **Symptom Checker** — covers 88 conditions across physical illness (76
   conditions: cold, flu, COVID-19, migraine, chickenpox, croup, measles,
   meningitis, Lyme disease, strep throat, ringworm, pinkeye, and more,
   informed by AAP/state-health-department childcare illness references,
   plus well-known global viral illnesses like Ebola, Zika, Dengue,
   Chikungunya, Yellow Fever, Rabies, HIV, and viral hepatitis) and mental
   health (12 conditions: depression, anxiety, PTSD, OCD, bipolar disorder,
   ADHD, etc.), with a multi-select symptom picker (250+ symptom labels),
   ranked matches with a match-score bar, matched/missing
   symptoms, suggested next steps, a Mayo Clinic summary per condition, and
   an automatic safety banner with crisis hotline info if emergency
   symptoms are selected (chest pain, stiff neck, severe bleeding, etc.).
3. **AI Assistant** — a RAG-powered chat that answers questions grounded in
   documents loaded into a local knowledge base (see setup below). Falls
   back to a clear setup message if not configured.
4. **Mental Health Check-In** — a private, adult self-check-in inspired by
   the widely used PHQ-9 (depression) and GAD-7 (anxiety) clinical
   screening questionnaires, paraphrased for general wellness use. Scores
   two indicators (Depression 0-27, Anxiety 0-12) into standard severity
   bands, links to the relevant condition write-up, and always shows crisis
   resources — never a diagnosis.
5. **Games & Breathing** — lightweight, non-clinical stress-relief tools:
   guided breathing with an animated circle (Box Breathing, 4-7-8, and Deep
   Belly Breathing patterns), a 5-4-3-2-1 grounding exercise, a bubble-pop
   fidget game, a gratitude jar, and gentle affirmations. Always available
   with no setup, and fully translated (hand-translated, no AI Assistant
   required).
6. **Upload Documents** — a password-gated page to add `.txt`, `.md`, or
   `.pdf` files to the shared knowledge base the AI Assistant searches.
7. **Find a Hospital** — click "Use my location" (uses your browser's
   geolocation) or type a city/address/zip, and see nearby hospitals on a
   free map with a distance-sorted list (address, phone, one-tap
   directions). Uses OpenStreetMap's free Nominatim (geocoding) and
   Overpass (place search) APIs — no API key or account needed.

## Running locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

The Kids Check-In, Symptom Checker, and Find a Hospital tabs work with no
further setup (Find a Hospital just needs normal internet access, and
browser geolocation for "Use my location" needs a secure context — HTTPS,
or `localhost` during local development — plus the user granting
permission when prompted). The AI Assistant and Upload Documents tabs need
the setup below.

## AI Assistant setup (optional)

The AI Assistant stores document embeddings in a local file
(`data/knowledge_base.json`, gitignored) — no external database or account
needed. It uses Claude (Anthropic) for chat answers and a local
sentence-transformers model for embeddings, so only one API key is needed.

1. Copy `.streamlit/secrets.toml.example` to `.streamlit/secrets.toml`
   (already gitignored) and fill in:
   - `ANTHROPIC_API_KEY` — an Anthropic API key
   - `ADMIN_PASSWORD` — a password of your choosing; required to use the
     Upload Documents tab, since uploaded documents are shared with every
     visitor's AI Assistant
2. Restart the app. Use the password-gated Upload Documents tab to add
   `.txt`, `.md`, or `.pdf` files to the knowledge base, then ask questions
   in the AI Assistant tab.

Without `ANTHROPIC_API_KEY` configured, the AI Assistant and Upload
Documents tabs show a setup message and the rest of the app works normally.
Two notes:
- The knowledge base lives on local disk, so it persists only for the
  lifetime of the running app process — redeploying resets it.
- The first embedding call downloads the local model (~90MB) if it isn't
  already cached, so the first upload or question may take longer.

## How it works

Each condition in `health_data.py` has a list of typical symptoms. When you
select your symptoms, the app scores every condition by how much its symptom
list overlaps with your selection (weighted toward recall — how much of the
condition's typical profile you match) and shows the top matches.

## Languages

A language picker in the sidebar (🌐) supports English, Spanish, French, and
Hindi:

- All UI chrome, navigation, and safety-critical text (crisis hotlines,
  emergency messages, urgency labels) is hand-translated in `i18n.py` and
  always available with no setup.
- The larger dynamic content — the 88 condition descriptions, the symptom
  vocabulary, the Kids Check-In questions/themes, and the Mental Health
  Check-In questions — is translated on first use via the configured AI
  Assistant (`translate.py`, two API calls: diseases+symptoms is the bulk,
  Kids/Mental-Health content is much smaller) and cached to disk per
  language (`data/translations/{lang}.json`, gitignored), so each language
  is only translated once. Symptom matching in the Symptom Checker still
  works correctly in any language, since the translated symptom labels are
  substituted consistently everywhere they appear.
- Without `ANTHROPIC_API_KEY` configured, switching languages still
  translates the UI chrome, but the Symptom Checker, Kids Check-In, and
  Mental Health Check-In content show a note and fall back to English.
- The AI Assistant tab answers in whichever language is selected — no
  extra setup, it just tells Claude which language to reply in.

Adding another language is a one-line change: add its code and name to
`LANGUAGES` in `i18n.py`, then add hand-translated entries to the other
dicts in that file (`CATEGORY_LABELS`, `URGENCY_LABELS_I18N`,
`EMERGENCY_MESSAGES_I18N`, `CRISIS_RESOURCES_I18N`, `UI_STRINGS`,
`KIDS_RESOURCE_DETAILS_I18N`) — the dynamic content translates itself
automatically the first time that language is used.
