"""Hand-translated UI strings for the app's chrome and safety-critical content.

These are always available with no API key required. Larger content bodies
(disease descriptions, Kids Check-In blurbs, symptom labels) are translated
dynamically via translate.py, which requires the AI Assistant to be
configured and falls back to English when it isn't.
"""

LANGUAGES = {
    "en": "English",
    "es": "Español",
    "fr": "Français",
    "hi": "हिन्दी",
}

CATEGORY_LABELS = {
    "en": {"Physical": "Physical", "Mental": "Mental"},
    "es": {"Physical": "Física", "Mental": "Mental"},
    "fr": {"Physical": "Physique", "Mental": "Mentale"},
    "hi": {"Physical": "शारीरिक", "Mental": "मानसिक"},
}

URGENCY_LABELS_I18N = {
    "en": {
        "emergency": "🚨 Seek immediate care",
        "see_doctor": "🩺 See a doctor",
        "self_care": "🏠 Usually self-care",
    },
    "es": {
        "emergency": "🚨 Busca atención inmediata",
        "see_doctor": "🩺 Consulta a un médico",
        "self_care": "🏠 Generalmente autocuidado",
    },
    "fr": {
        "emergency": "🚨 Consultez immédiatement",
        "see_doctor": "🩺 Consultez un médecin",
        "self_care": "🏠 Soins personnels généralement",
    },
    "hi": {
        "emergency": "🚨 तुरंत चिकित्सा सहायता लें",
        "see_doctor": "🩺 डॉक्टर से मिलें",
        "self_care": "🏠 आमतौर पर स्व-देखभाल",
    },
}

# Messages shown for EMERGENCY_SYMPTOMS keys (health_data.py) — safety-critical,
# always available without an API key.
EMERGENCY_MESSAGES_I18N = {
    "en": {
        "thoughts of death": "You mentioned thoughts of death or self-harm.",
        "thoughts of self-harm or suicide": "You mentioned thoughts of self-harm or suicide.",
        "chest pain": "Chest pain can be a sign of a medical emergency.",
        "severe difficulty breathing": "Severe difficulty breathing needs immediate attention.",
        "sudden numbness or weakness on one side": "This can be a sign of a stroke.",
        "loss of consciousness": "Loss of consciousness needs immediate medical attention.",
        "severe uncontrolled bleeding": "Severe bleeding needs immediate medical attention.",
    },
    "es": {
        "thoughts of death": "Mencionaste pensamientos de muerte o autolesión.",
        "thoughts of self-harm or suicide": "Mencionaste pensamientos de autolesión o suicidio.",
        "chest pain": "El dolor en el pecho puede ser señal de una emergencia médica.",
        "severe difficulty breathing": "La dificultad grave para respirar necesita atención inmediata.",
        "sudden numbness or weakness on one side": "Esto puede ser señal de un derrame cerebral.",
        "loss of consciousness": "La pérdida del conocimiento necesita atención médica inmediata.",
        "severe uncontrolled bleeding": "El sangrado severo necesita atención médica inmediata.",
    },
    "fr": {
        "thoughts of death": "Vous avez mentionné des pensées de mort ou d'automutilation.",
        "thoughts of self-harm or suicide": "Vous avez mentionné des pensées d'automutilation ou de suicide.",
        "chest pain": "Une douleur thoracique peut être le signe d'une urgence médicale.",
        "severe difficulty breathing": "Une difficulté respiratoire sévère nécessite une attention immédiate.",
        "sudden numbness or weakness on one side": "Cela peut être un signe d'AVC.",
        "loss of consciousness": "Une perte de conscience nécessite des soins médicaux immédiats.",
        "severe uncontrolled bleeding": "Un saignement sévère nécessite des soins médicaux immédiats.",
    },
    "hi": {
        "thoughts of death": "आपने मृत्यु या स्वयं को नुकसान पहुँचाने के विचारों का उल्लेख किया।",
        "thoughts of self-harm or suicide": "आपने आत्म-हानि या आत्महत्या के विचारों का उल्लेख किया।",
        "chest pain": "सीने में दर्द चिकित्सा आपातकाल का संकेत हो सकता है।",
        "severe difficulty breathing": "सांस लेने में गंभीर कठिनाई पर तुरंत ध्यान देने की आवश्यकता है।",
        "sudden numbness or weakness on one side": "यह स्ट्रोक का संकेत हो सकता है।",
        "loss of consciousness": "बेहोशी पर तुरंत चिकित्सा ध्यान देने की आवश्यकता है।",
        "severe uncontrolled bleeding": "गंभीर रक्तस्राव पर तुरंत चिकित्सा ध्यान देने की आवश्यकता है।",
    },
}

# (label, detail) pairs mirroring health_data.CRISIS_RESOURCES, one per language.
CRISIS_RESOURCES_I18N = {
    "en": [
        ("US — 988 Suicide & Crisis Lifeline", "Call or text 988 (24/7)"),
        ("US — Crisis Text Line", "Text HOME to 741741"),
        ("International Association for Suicide Prevention", "https://www.iasp.info/resources/Crisis_Centres/"),
        ("Emergency services", "If you are in immediate danger, call your local emergency number (e.g., 911/112/999)."),
    ],
    "es": [
        ("EE. UU. — Línea 988 de Prevención del Suicidio y Crisis", "Llama o envía un mensaje al 988 (24/7)"),
        ("EE. UU. — Crisis Text Line", "Envía HOME al 741741"),
        ("Asociación Internacional para la Prevención del Suicidio", "https://www.iasp.info/resources/Crisis_Centres/"),
        ("Servicios de emergencia", "Si estás en peligro inmediato, llama al número de emergencia local (p. ej., 911/112/999)."),
    ],
    "fr": [
        ("États-Unis — Ligne 988 Suicide & Crise", "Appelez ou envoyez un SMS au 988 (24/7)"),
        ("États-Unis — Crisis Text Line", "Envoyez HOME au 741741"),
        ("Association internationale pour la prévention du suicide", "https://www.iasp.info/resources/Crisis_Centres/"),
        ("Services d'urgence", "En cas de danger immédiat, appelez votre numéro d'urgence local (ex. : 911/112/999)."),
    ],
    "hi": [
        ("अमेरिका — 988 सुसाइड एंड क्राइसिस लाइफलाइन", "988 पर कॉल या टेक्स्ट करें (24/7)"),
        ("अमेरिका — क्राइसिस टेक्स्ट लाइन", "741741 पर HOME लिखकर भेजें"),
        ("इंटरनेशनल एसोसिएशन फॉर सुसाइड प्रिवेंशन", "https://www.iasp.info/resources/Crisis_Centres/"),
        ("आपातकालीन सेवाएँ", "यदि आप तत्काल खतरे में हैं, तो अपने स्थानीय आपातकालीन नंबर पर कॉल करें (जैसे 911/112/999)।"),
    ],
}

UI_STRINGS = {
    "en": {
        "language_label": "🌐 Language",
        "app_caption": (
            "A friendly check-in for kids & teens, plus a rule-based symptom-overlap tool for "
            "physical and mental health. Neither is a diagnosis."
        ),
        "breadcrumb": "Home &nbsp;›&nbsp; Diseases &amp; Conditions &nbsp;›&nbsp; Symptom &amp; Wellness Checker",
        "topbar": "🩺&nbsp; Symptom &amp; Wellness Checker",
        "hero_explore_label": "Explore this app",
        "footer": (
            "Built for educational/hackathon purposes. Always consult a licensed medical "
            "or mental health professional for real diagnosis and treatment."
        ),
        "translation_fallback_note": (
            "🌐 Full translation of this content needs the AI Assistant configured "
            "(see the AI Assistant tab) — showing English for now."
        ),
        "sidebar_filters_header": "Filters",
        "sidebar_filters_caption": "Applies to the Symptom Checker tab.",
        "sidebar_categories_label": "Which areas do you want to check?",
        "sidebar_select_category_warning": "Select at least one category to continue.",
        "sidebar_about_header": "About",
        "sidebar_about_text": (
            "This checker cross-references the symptoms you select against a curated "
            "list of **{total} conditions** ({physical} physical, {mental} mental health) "
            "and ranks them by how closely your symptoms match each condition's typical profile."
        ),
        "tab_kids": "🧒 Kids & Teens Check-In",
        "tab_checker": "🔍 Symptom Checker",
        "tab_assistant": "🤖 AI Assistant",
        "tab_upload": "📄 Upload Documents",
        "tab_hospital": "🏥 Find a Hospital",
        "kids_subheader": "A quick, friendly check-in",
        "kids_caption": (
            "This isn't a test, a score, or a diagnosis — just a few questions to help you notice "
            "how you've been feeling lately. Answer honestly. Nothing here is judged, and your "
            "answers aren't saved anywhere."
        ),
        "kids_one_more_question": (
            "**One more question.** This one's just about keeping you safe — it's always okay "
            "to answer honestly."
        ),
        "kids_submit_button": "See what this might mean",
        "kids_safety_alert_title": "💙 Your safety matters most right now",
        "kids_safety_alert_body": (
            "Thank you for being honest — that takes courage. Please tell a trusted adult "
            "right away (a parent, relative, teacher, or school counselor), or reach out now:"
        ),
        "kids_988_line": (
            "**[988 Suicide & Crisis Lifeline](https://988lifeline.org/)**: Call or text 988 — "
            "free, confidential, 24/7."
        ),
        "kids_crisis_text_line": (
            "**[Crisis Text Line](https://www.crisistextline.org/)**: Text HOME to 741741 — free, 24/7."
        ),
        "kids_what_we_noticed": "#### What we noticed",
        "kids_answer_prompt": "Answer a few questions above to see your check-in summary.",
        "kids_steady": (
            "Based on your answers, things sound fairly steady right now. That's great — "
            "and it's always okay to check in with someone you trust if that changes."
        ),
        "kids_learn_more": "Learn more",
        "kids_resources_header": "#### Resources for you",
        "kids_footer_note": (
            "This check-in is not a diagnosis and doesn't replace talking to a real person. "
            "A parent, relative, teacher, school counselor, or doctor can help you figure out "
            "what to do next."
        ),
        "answer_not_really": "Not really",
        "answer_sometimes": "Sometimes",
        "answer_a_lot": "A lot",
        "checker_disclaimer_title": "⚠️ Important disclaimer — please read",
        "checker_disclaimer_body": (
            "This tool is for **educational purposes only** and does not provide medical "
            "or mental health advice, diagnosis, or treatment. It uses simple symptom "
            "matching, not a clinical or AI model. Always consult a qualified doctor or "
            "mental health professional for any health concern. If you believe you are "
            "having a medical or mental health emergency, contact your local emergency "
            "services immediately."
        ),
        "checker_step1": "1. Select your symptoms",
        "checker_multiselect_label": "Start typing to search, or scroll to browse. Select as many as apply.",
        "checker_multiselect_placeholder": "🔍  e.g. persistent sadness, headache, shortness of breath...",
        "checker_analyze_button": "Analyze symptoms",
        "checker_emergency_title": "### 🚨 This may be a medical emergency",
        "checker_emergency_seek_help": "**Please seek immediate help. Crisis and emergency resources:**",
        "checker_step2": "2. Possible matches",
        "checker_select_prompt": "Select one or more symptoms above, then click **Analyze symptoms**.",
        "checker_no_matches": "No matching conditions found for the selected symptoms in this reference set.",
        "checker_category_label": "Category: {category}",
        "checker_match_score": "Match score: {pct}%",
        "checker_matched_symptoms": "✅ **Matched symptoms:** {symptoms}",
        "checker_missing_symptoms": "ℹ️ **Other typical symptoms not selected:** {symptoms}",
        "checker_suggested_next_step": "**Suggested next step:** {advice}",
        "checker_mayo_expander": "📖 AI summary from Mayo Clinic",
        "checker_mayo_source": "Source: [Mayo Clinic]({url})",
        "checker_footer_note": (
            "Results are ranked by symptom overlap only and may include conditions "
            "that are not relevant to you. This is not a diagnosis — please consult "
            "a healthcare professional to confirm any condition."
        ),
        "tab_mental_health": "🧠 Mental Health Check-In",
        "mh_subheader": "A moment for your mental health",
        "mh_caption": (
            "A short, private self-check-in inspired by widely used clinical screening "
            "questionnaires (PHQ-9 for mood, GAD-7 for anxiety). It's not a diagnosis — "
            "just a way to notice patterns worth talking to a professional about."
        ),
        "mh_disclaimer_title": "⚠️ Important disclaimer — please read",
        "mh_disclaimer_body": (
            "This check-in is for **educational and self-reflection purposes only**. It is "
            "inspired by standard screening questionnaires used in clinical settings, but "
            "taking it here does not diagnose any condition. Only a qualified mental health "
            "professional can provide a diagnosis. If you're in crisis or thinking about "
            "harming yourself, please contact the resources below right away."
        ),
        "mh_depression_header": "Over the last 2 weeks, how often have you been bothered by any of the following?",
        "mh_anxiety_header": "And how often have you been bothered by these?",
        "mh_one_more_question": (
            "**One more question.** This one's just about keeping you safe — it's always okay "
            "to answer honestly."
        ),
        "mh_submit_button": "See my results",
        "mh_safety_alert_body": (
            "Thank you for being honest — that takes courage. Please reach out to one of the "
            "resources below right now, or contact someone you trust:"
        ),
        "mh_prompt": "Answer the questions above, then click **See my results**.",
        "mh_results_header": "#### Your check-in results",
        "mh_depression_result": "Depression indicator: **{label}** ({score}/27)",
        "mh_anxiety_result": "Anxiety indicator: **{label}** ({score}/12)",
        "mh_results_note": (
            "These are screening indicators only, inspired by standard clinical "
            "questionnaires — not a diagnosis. A mental health professional can give you a "
            "real evaluation and talk through what these patterns might mean for you."
        ),
        "mh_learn_more_depression": "📖 Learn more about depression",
        "mh_learn_more_anxiety": "📖 Learn more about anxiety",
        "mh_resources_header": "#### Resources",
        "mh_footer_note": (
            "This check-in does not replace a conversation with a licensed mental health "
            "professional. If anything here concerns you, please reach out for support."
        ),
        "tab_games": "🧘 Games & Breathing",
        "games_subheader": "Take a breather",
        "games_caption": (
            "A few simple, non-clinical tools for stress relief — guided breathing, a "
            "grounding exercise, a stress-relief bubble popper, a gratitude jar, and "
            "gentle affirmations. Not a treatment or substitute for professional care."
        ),
        "games_breathing_header": "🌬️ Guided breathing",
        "games_breathing_select_label": "Choose a breathing pattern",
        "games_breathing_hint": "Follow the circle: grow as you breathe in, hold, shrink as you breathe out, hold.",
        "games_phase_inhale": "Inhale",
        "games_phase_hold": "Hold",
        "games_phase_exhale": "Exhale",
        "games_grounding_header": "🌳 5-4-3-2-1 grounding exercise",
        "games_grounding_caption": (
            "A classic grounding technique to help settle a busy mind by noticing your "
            "surroundings through your senses."
        ),
        "games_grounding_complete": "Nice work grounding yourself in the present moment. 🌿",
        "games_bubbles_header": "🫧 Bubble pop",
        "games_bubbles_caption": "A little fidget toy — pop a few bubbles to blow off some steam.",
        "games_bubbles_counter": "Popped: {popped} / {total}",
        "games_bubbles_reset": "Refill bubbles",
        "games_gratitude_header": "📝 Gratitude jar",
        "games_gratitude_caption": "Jot down a few small things you're grateful for today.",
        "games_gratitude_placeholder": "Something you're grateful for...",
        "games_gratitude_add": "Add to jar",
        "games_gratitude_clear": "Clear jar",
        "games_gratitude_empty": "Your jar is empty — add something small and good from today.",
        "games_affirmation_header": "💛 Gentle affirmations",
        "games_affirmation_caption": "A little reminder, whenever you need one.",
        "games_affirmation_button": "Show me an affirmation",
        "games_footer_note": (
            "These are simple relaxation tools, not therapy or medical treatment. If you're "
            "struggling, the Mental Health Check-In tab has resources, including the 988 "
            "Suicide & Crisis Lifeline."
        ),
        "assistant_subheader": "Ask a question",
        "assistant_caption": (
            "A healthcare-savvy AI assistant grounded in this app's own condition data — plus "
            "anything extra loaded into the knowledge base (see the Upload Documents tab) — and "
            "backed by general medical/mental-health knowledge for anything else. This is not a "
            "diagnosis and does not replace a real conversation with a qualified professional."
        ),
        "assistant_not_configured": (
            "The AI Assistant isn't set up yet. Add `ANTHROPIC_API_KEY` to "
            "`.streamlit/secrets.toml` — see `.streamlit/secrets.toml.example` for setup."
        ),
        "assistant_preparing_kb": "Preparing knowledge base...",
        "assistant_chat_placeholder": "Ask a health question...",
        "assistant_crisis_answer": (
            "I noticed your question may involve thoughts of self-harm or crisis. "
            "Please reach out to the resources above right away — a real person "
            "can help in a way I can't."
        ),
        "assistant_thinking": "Thinking...",
        "assistant_error_prefix": "Something went wrong answering that: {error}",
        "assistant_sources_prefix": "Sources: {sources}",
        "upload_subheader": "Load a document into the knowledge base",
        "upload_caption": (
            "Documents uploaded here are shared with every visitor's AI Assistant — "
            "they're added to a knowledge base, not kept private to your session."
        ),
        "upload_not_configured": (
            "Document upload isn't set up yet. Add `ANTHROPIC_API_KEY` to "
            "`.streamlit/secrets.toml` — see `.streamlit/secrets.toml.example` for setup."
        ),
        "upload_kb_stats": "Knowledge base currently has **{chunks}** chunks from **{documents}** document(s).",
        "upload_set_password": "Set `ADMIN_PASSWORD` in secrets to enable document uploads.",
        "upload_password_label": "Admin password",
        "upload_file_uploader_label": "Upload .txt, .md, or .pdf files",
        "upload_add_button": "Add to knowledge base",
        "upload_processing": "Processing {filename}...",
        "upload_error": "Couldn't add {filename}: {error}",
        "upload_success": "Added {filename} ({count} chunks).",
        "upload_incorrect_password": "Incorrect password.",
        "hospital_subheader": "Find a nearby hospital",
        "hospital_caption": (
            "Click \"Use my location\" or enter a city/address to see nearby hospitals on a "
            "free map, using OpenStreetMap data — no account or API key needed. **If this is "
            "a real emergency, call your local emergency number (e.g. 911/112/999) instead of "
            "waiting on this page.**"
        ),
        "hospital_use_location_button": "📍 Use my location",
        "hospital_manual_location_label": "Or enter a city, address, or zip code",
        "hospital_manual_location_placeholder": "e.g. Boston, MA",
        "hospital_search_button": "Search this location",
        "hospital_radius_label": "Search radius (km)",
        "hospital_getting_location": "Getting your location...",
        "hospital_geo_error": (
            "Couldn't get your location ({error}). Allow location access in your browser, "
            "or search by address instead."
        ),
        "hospital_your_location_label": "your current location",
        "hospital_looking_up": "Looking up that location...",
        "hospital_geocode_service_error": (
            "Couldn't reach the location service. Check your internet connection and try again."
        ),
        "hospital_not_found": "Couldn't find that location. Try a more specific address or city.",
        "hospital_searching": "Searching for nearby hospitals...",
        "hospital_search_service_error": (
            "Couldn't reach the hospital search service. Check your internet connection and try again."
        ),
        "hospital_showing_results": "📍 Showing results near **{location}**",
        "hospital_no_results": "No hospitals found in this radius. Try increasing the search radius.",
        "hospital_distance_away": "**{distance} km away**",
        "hospital_has_er": "🚨 **Has an emergency department**",
        "hospital_get_directions": "[Get directions ↗]({url})",
        "hospital_prompt": "Click **Use my location** or search an address to see nearby hospitals.",
    },
}

# ---------------------------------------------------------------------------
# Spanish, French, German, Portuguese, Hindi, Chinese translations of every
# key above (same keys, translated values). Placeholders like {total} must
# stay unchanged.
# ---------------------------------------------------------------------------

UI_STRINGS["es"] = {
    "language_label": "🌐 Idioma",
    "app_caption": (
        "Un espacio amigable para niños y adolescentes, además de una herramienta basada en "
        "reglas para comparar síntomas físicos y de salud mental. Ninguno es un diagnóstico."
    ),
    "breadcrumb": "Inicio &nbsp;›&nbsp; Enfermedades y afecciones &nbsp;›&nbsp; Verificador de síntomas y bienestar",
    "topbar": "🩺&nbsp; Verificador de síntomas y bienestar",
    "hero_explore_label": "Explorar esta app",
    "footer": (
        "Creado con fines educativos/de hackathon. Consulta siempre a un profesional médico "
        "o de salud mental con licencia para un diagnóstico y tratamiento reales."
    ),
    "translation_fallback_note": (
        "🌐 La traducción completa de este contenido requiere configurar el Asistente de IA "
        "(ver la pestaña Asistente de IA) — mostrando inglés por ahora."
    ),
    "sidebar_filters_header": "Filtros",
    "sidebar_filters_caption": "Se aplica a la pestaña Verificador de síntomas.",
    "sidebar_categories_label": "¿Qué áreas quieres revisar?",
    "sidebar_select_category_warning": "Selecciona al menos una categoría para continuar.",
    "sidebar_about_header": "Acerca de",
    "sidebar_about_text": (
        "Este verificador compara los síntomas que seleccionas con una lista curada de "
        "**{total} afecciones** ({physical} físicas, {mental} de salud mental) y las clasifica "
        "según qué tan bien coinciden tus síntomas con el perfil típico de cada afección."
    ),
    "tab_kids": "🧒 Chequeo para niños y adolescentes",
    "tab_checker": "🔍 Verificador de síntomas",
    "tab_assistant": "🤖 Asistente de IA",
    "tab_upload": "📄 Subir documentos",
    "tab_hospital": "🏥 Encontrar un hospital",
    "kids_subheader": "Un chequeo rápido y amigable",
    "kids_caption": (
        "Esto no es una prueba, ni una puntuación, ni un diagnóstico — solo unas preguntas para "
        "ayudarte a notar cómo te has sentido últimamente. Responde con honestidad. Nada aquí se "
        "juzga, y tus respuestas no se guardan en ningún lugar."
    ),
    "kids_one_more_question": (
        "**Una pregunta más.** Esta es solo para cuidar tu seguridad — siempre está bien "
        "responder con honestidad."
    ),
    "kids_submit_button": "Ver qué podría significar esto",
    "kids_safety_alert_title": "💙 Tu seguridad es lo más importante ahora mismo",
    "kids_safety_alert_body": (
        "Gracias por ser honesto/a — eso requiere valentía. Cuéntaselo a un adulto de confianza "
        "de inmediato (un padre, familiar, maestro o consejero escolar), o busca ayuda ahora mismo:"
    ),
    "kids_988_line": (
        "**[Línea 988 de Prevención del Suicidio y Crisis](https://988lifeline.org/)**: Llama o "
        "envía un mensaje al 988 — gratis, confidencial, 24/7."
    ),
    "kids_crisis_text_line": (
        "**[Crisis Text Line](https://www.crisistextline.org/)**: Envía HOME al 741741 — gratis, 24/7."
    ),
    "kids_what_we_noticed": "#### Lo que notamos",
    "kids_answer_prompt": "Responde algunas preguntas arriba para ver tu resumen del chequeo.",
    "kids_steady": (
        "Según tus respuestas, las cosas parecen estar bastante estables ahora mismo. Eso es "
        "genial — y siempre está bien hablar con alguien de confianza si eso cambia."
    ),
    "kids_learn_more": "Más información",
    "kids_resources_header": "#### Recursos para ti",
    "kids_footer_note": (
        "Este chequeo no es un diagnóstico y no reemplaza hablar con una persona real. Un padre, "
        "familiar, maestro, consejero escolar o médico puede ayudarte a decidir qué hacer después."
    ),
    "answer_not_really": "No mucho",
    "answer_sometimes": "A veces",
    "answer_a_lot": "Mucho",
    "checker_disclaimer_title": "⚠️ Aviso importante — por favor lee esto",
    "checker_disclaimer_body": (
        "Esta herramienta es **solo con fines educativos** y no proporciona asesoramiento, "
        "diagnóstico ni tratamiento médico o de salud mental. Utiliza una simple coincidencia "
        "de síntomas, no un modelo clínico o de IA. Consulta siempre a un médico o profesional "
        "de salud mental calificado ante cualquier inquietud de salud. Si crees que estás "
        "teniendo una emergencia médica o de salud mental, contacta a los servicios de "
        "emergencia locales de inmediato."
    ),
    "checker_step1": "1. Selecciona tus síntomas",
    "checker_multiselect_label": "Empieza a escribir para buscar, o desplázate para explorar. Selecciona todos los que apliquen.",
    "checker_multiselect_placeholder": "🔍  p. ej. tristeza persistente, dolor de cabeza, dificultad para respirar...",
    "checker_analyze_button": "Analizar síntomas",
    "checker_emergency_title": "### 🚨 Esto podría ser una emergencia médica",
    "checker_emergency_seek_help": "**Busca ayuda de inmediato. Recursos de crisis y emergencia:**",
    "checker_step2": "2. Posibles coincidencias",
    "checker_select_prompt": "Selecciona uno o más síntomas arriba y haz clic en **Analizar síntomas**.",
    "checker_no_matches": "No se encontraron afecciones que coincidan con los síntomas seleccionados en este conjunto de referencia.",
    "checker_category_label": "Categoría: {category}",
    "checker_match_score": "Puntaje de coincidencia: {pct}%",
    "checker_matched_symptoms": "✅ **Síntomas coincidentes:** {symptoms}",
    "checker_missing_symptoms": "ℹ️ **Otros síntomas típicos no seleccionados:** {symptoms}",
    "checker_suggested_next_step": "**Próximo paso sugerido:** {advice}",
    "checker_mayo_expander": "📖 Resumen de IA de Mayo Clinic",
    "checker_mayo_source": "Fuente: [Mayo Clinic]({url})",
    "checker_footer_note": (
        "Los resultados se clasifican solo según la coincidencia de síntomas y pueden incluir "
        "afecciones que no sean relevantes para ti. Esto no es un diagnóstico — consulta a un "
        "profesional de la salud para confirmar cualquier afección."
    ),
    "tab_mental_health": "🧠 Chequeo de salud mental",
    "mh_subheader": "Un momento para tu salud mental",
    "mh_caption": (
        "Un chequeo breve y privado inspirado en cuestionarios de detección clínica "
        "ampliamente usados (PHQ-9 para el estado de ánimo, GAD-7 para la ansiedad). No es "
        "un diagnóstico — solo una forma de notar patrones que vale la pena comentar con un "
        "profesional."
    ),
    "mh_disclaimer_title": "⚠️ Aviso importante — por favor lee esto",
    "mh_disclaimer_body": (
        "Este chequeo es **solo con fines educativos y de autorreflexión**. Está inspirado "
        "en cuestionarios de detección estándar usados en entornos clínicos, pero "
        "responderlo aquí no diagnostica ninguna afección. Solo un profesional de salud "
        "mental calificado puede dar un diagnóstico. Si estás en crisis o pensando en "
        "hacerte daño, por favor contacta los recursos de abajo de inmediato."
    ),
    "mh_depression_header": "En las últimas 2 semanas, ¿con qué frecuencia te ha molestado alguno de los siguientes?",
    "mh_anxiety_header": "¿Y con qué frecuencia te ha molestado esto?",
    "mh_one_more_question": (
        "**Una pregunta más.** Esta es solo para cuidar tu seguridad — siempre está bien "
        "responder con honestidad."
    ),
    "mh_submit_button": "Ver mis resultados",
    "mh_safety_alert_body": (
        "Gracias por ser honesto/a — eso requiere valentía. Por favor contacta uno de los "
        "recursos de abajo ahora mismo, o comunícate con alguien de confianza:"
    ),
    "mh_prompt": "Responde las preguntas de arriba y luego haz clic en **Ver mis resultados**.",
    "mh_results_header": "#### Resultados de tu chequeo",
    "mh_depression_result": "Indicador de depresión: **{label}** ({score}/27)",
    "mh_anxiety_result": "Indicador de ansiedad: **{label}** ({score}/12)",
    "mh_results_note": (
        "Estos son solo indicadores de detección, inspirados en cuestionarios clínicos "
        "estándar — no un diagnóstico. Un profesional de salud mental puede darte una "
        "evaluación real y hablar sobre lo que estos patrones podrían significar para ti."
    ),
    "mh_learn_more_depression": "📖 Más información sobre la depresión",
    "mh_learn_more_anxiety": "📖 Más información sobre la ansiedad",
    "mh_resources_header": "#### Recursos",
    "mh_footer_note": (
        "Este chequeo no reemplaza una conversación con un profesional de salud mental con "
        "licencia. Si algo aquí te preocupa, por favor busca apoyo."
    ),
    "tab_games": "🧘 Juegos y respiración",
    "games_subheader": "Tómate un respiro",
    "games_caption": (
        "Algunas herramientas simples y no clínicas para aliviar el estrés: respiración "
        "guiada, un ejercicio de conexión con el presente, un juego de burbujas "
        "antiestrés, un frasco de gratitud y afirmaciones suaves. No es un tratamiento ni "
        "sustituye la atención profesional."
    ),
    "games_breathing_header": "🌬️ Respiración guiada",
    "games_breathing_select_label": "Elige un patrón de respiración",
    "games_breathing_hint": "Sigue el círculo: crece al inhalar, se mantiene, se encoge al exhalar, se mantiene.",
    "games_phase_inhale": "Inhala",
    "games_phase_hold": "Mantén",
    "games_phase_exhale": "Exhala",
    "games_grounding_header": "🌳 Ejercicio de conexión 5-4-3-2-1",
    "games_grounding_caption": (
        "Una técnica clásica para calmar una mente ocupada notando tu entorno a través de "
        "los sentidos."
    ),
    "games_grounding_complete": "Buen trabajo conectando con el presente. 🌿",
    "games_bubbles_header": "🫧 Burbujas antiestrés",
    "games_bubbles_caption": "Un pequeño juego para las manos — revienta algunas burbujas para liberar tensión.",
    "games_bubbles_counter": "Reventadas: {popped} / {total}",
    "games_bubbles_reset": "Rellenar burbujas",
    "games_gratitude_header": "📝 Frasco de gratitud",
    "games_gratitude_caption": "Anota algunas cosas pequeñas por las que estás agradecido hoy.",
    "games_gratitude_placeholder": "Algo por lo que estás agradecido...",
    "games_gratitude_add": "Añadir al frasco",
    "games_gratitude_clear": "Vaciar frasco",
    "games_gratitude_empty": "Tu frasco está vacío — añade algo pequeño y bueno de hoy.",
    "games_affirmation_header": "💛 Afirmaciones suaves",
    "games_affirmation_caption": "Un pequeño recordatorio, cuando lo necesites.",
    "games_affirmation_button": "Muéstrame una afirmación",
    "games_footer_note": (
        "Estas son herramientas de relajación simples, no terapia ni tratamiento médico. Si "
        "estás pasando por un momento difícil, la pestaña de Chequeo de salud mental tiene "
        "recursos, incluida la línea 988 de Suicidio y Crisis."
    ),
    "assistant_subheader": "Haz una pregunta",
    "assistant_caption": (
        "Un asistente de IA con conocimientos de salud, basado en los datos propios de "
        "afecciones de esta app — más cualquier contenido adicional cargado en la base de "
        "conocimiento (ver la pestaña Subir documentos) — y respaldado por conocimiento médico "
        "y de salud mental general para todo lo demás. Esto no es un diagnóstico y no reemplaza "
        "una conversación real con un profesional calificado."
    ),
    "assistant_not_configured": (
        "El Asistente de IA aún no está configurado. Agrega `ANTHROPIC_API_KEY` a "
        "`.streamlit/secrets.toml` — consulta `.streamlit/secrets.toml.example` para la configuración."
    ),
    "assistant_preparing_kb": "Preparando la base de conocimiento...",
    "assistant_chat_placeholder": "Haz una pregunta de salud...",
    "assistant_crisis_answer": (
        "Noté que tu pregunta podría involucrar pensamientos de autolesión o crisis. Por favor "
        "contacta los recursos de arriba de inmediato — una persona real puede ayudarte de una "
        "forma en que yo no puedo."
    ),
    "assistant_thinking": "Pensando...",
    "assistant_error_prefix": "Algo salió mal al responder eso: {error}",
    "assistant_sources_prefix": "Fuentes: {sources}",
    "upload_subheader": "Cargar un documento en la base de conocimiento",
    "upload_caption": (
        "Los documentos cargados aquí se comparten con el Asistente de IA de todos los "
        "visitantes — se agregan a una base de conocimiento, no se mantienen privados de tu sesión."
    ),
    "upload_not_configured": (
        "La carga de documentos aún no está configurada. Agrega `ANTHROPIC_API_KEY` a "
        "`.streamlit/secrets.toml` — consulta `.streamlit/secrets.toml.example` para la configuración."
    ),
    "upload_kb_stats": "La base de conocimiento tiene actualmente **{chunks}** fragmentos de **{documents}** documento(s).",
    "upload_set_password": "Configura `ADMIN_PASSWORD` en los secretos para habilitar la carga de documentos.",
    "upload_password_label": "Contraseña de administrador",
    "upload_file_uploader_label": "Sube archivos .txt, .md o .pdf",
    "upload_add_button": "Agregar a la base de conocimiento",
    "upload_processing": "Procesando {filename}...",
    "upload_error": "No se pudo agregar {filename}: {error}",
    "upload_success": "Se agregó {filename} ({count} fragmentos).",
    "upload_incorrect_password": "Contraseña incorrecta.",
    "hospital_subheader": "Encuentra un hospital cercano",
    "hospital_caption": (
        "Haz clic en \"Usar mi ubicación\" o ingresa una ciudad/dirección para ver hospitales "
        "cercanos en un mapa gratuito, usando datos de OpenStreetMap — sin cuenta ni clave de "
        "API necesaria. **Si esto es una emergencia real, llama a tu número de emergencia local "
        "(p. ej. 911/112/999) en lugar de esperar en esta página.**"
    ),
    "hospital_use_location_button": "📍 Usar mi ubicación",
    "hospital_manual_location_label": "O ingresa una ciudad, dirección o código postal",
    "hospital_manual_location_placeholder": "p. ej. Boston, MA",
    "hospital_search_button": "Buscar esta ubicación",
    "hospital_radius_label": "Radio de búsqueda (km)",
    "hospital_getting_location": "Obteniendo tu ubicación...",
    "hospital_geo_error": (
        "No se pudo obtener tu ubicación ({error}). Permite el acceso a la ubicación en tu "
        "navegador, o busca por dirección en su lugar."
    ),
    "hospital_your_location_label": "tu ubicación actual",
    "hospital_looking_up": "Buscando esa ubicación...",
    "hospital_geocode_service_error": (
        "No se pudo conectar con el servicio de ubicación. Revisa tu conexión a internet e "
        "intenta de nuevo."
    ),
    "hospital_not_found": "No se pudo encontrar esa ubicación. Prueba con una dirección o ciudad más específica.",
    "hospital_searching": "Buscando hospitales cercanos...",
    "hospital_search_service_error": (
        "No se pudo conectar con el servicio de búsqueda de hospitales. Revisa tu conexión a "
        "internet e intenta de nuevo."
    ),
    "hospital_showing_results": "📍 Mostrando resultados cerca de **{location}**",
    "hospital_no_results": "No se encontraron hospitales en este radio. Intenta aumentar el radio de búsqueda.",
    "hospital_distance_away": "**a {distance} km**",
    "hospital_has_er": "🚨 **Tiene sala de emergencias**",
    "hospital_get_directions": "[Obtener direcciones ↗]({url})",
    "hospital_prompt": "Haz clic en **Usar mi ubicación** o busca una dirección para ver hospitales cercanos.",
}

UI_STRINGS["fr"] = {
    "language_label": "🌐 Langue",
    "app_caption": (
        "Un espace bienveillant pour les enfants et les adolescents, ainsi qu'un outil basé sur "
        "des règles pour comparer les symptômes physiques et de santé mentale. Aucun des deux "
        "n'est un diagnostic."
    ),
    "breadcrumb": "Accueil &nbsp;›&nbsp; Maladies et affections &nbsp;›&nbsp; Vérificateur de symptômes et de bien-être",
    "topbar": "🩺&nbsp; Vérificateur de symptômes et de bien-être",
    "hero_explore_label": "Explorer cette appli",
    "footer": (
        "Conçu à des fins éducatives/hackathon. Consultez toujours un professionnel de santé "
        "ou de santé mentale agréé pour un véritable diagnostic et traitement."
    ),
    "translation_fallback_note": (
        "🌐 La traduction complète de ce contenu nécessite la configuration de l'Assistant IA "
        "(voir l'onglet Assistant IA) — affichage en anglais pour le moment."
    ),
    "sidebar_filters_header": "Filtres",
    "sidebar_filters_caption": "S'applique à l'onglet Vérificateur de symptômes.",
    "sidebar_categories_label": "Quels domaines voulez-vous vérifier ?",
    "sidebar_select_category_warning": "Sélectionnez au moins une catégorie pour continuer.",
    "sidebar_about_header": "À propos",
    "sidebar_about_text": (
        "Ce vérificateur compare les symptômes que vous sélectionnez à une liste organisée de "
        "**{total} affections** ({physical} physiques, {mental} de santé mentale) et les classe "
        "selon la correspondance avec le profil typique de chaque affection."
    ),
    "tab_kids": "🧒 Bilan pour enfants et ados",
    "tab_checker": "🔍 Vérificateur de symptômes",
    "tab_assistant": "🤖 Assistant IA",
    "tab_upload": "📄 Téléverser des documents",
    "tab_hospital": "🏥 Trouver un hôpital",
    "kids_subheader": "Un bilan rapide et bienveillant",
    "kids_caption": (
        "Ce n'est ni un test, ni un score, ni un diagnostic — juste quelques questions pour "
        "t'aider à remarquer comment tu te sens ces derniers temps. Réponds honnêtement. Rien "
        "ici n'est jugé, et tes réponses ne sont enregistrées nulle part."
    ),
    "kids_one_more_question": (
        "**Une dernière question.** Celle-ci concerne simplement ta sécurité — c'est toujours "
        "bien de répondre honnêtement."
    ),
    "kids_submit_button": "Voir ce que cela pourrait signifier",
    "kids_safety_alert_title": "💙 Ta sécurité compte le plus en ce moment",
    "kids_safety_alert_body": (
        "Merci d'avoir été honnête — cela demande du courage. Parles-en tout de suite à un "
        "adulte de confiance (un parent, un proche, un enseignant ou un conseiller scolaire), "
        "ou contacte l'un de ces services dès maintenant :"
    ),
    "kids_988_line": (
        "**[Ligne 988 Suicide & Crise](https://988lifeline.org/)** : Appelle ou envoie un SMS "
        "au 988 — gratuit, confidentiel, 24/7."
    ),
    "kids_crisis_text_line": (
        "**[Crisis Text Line](https://www.crisistextline.org/)** : Envoie HOME au 741741 — "
        "gratuit, 24/7."
    ),
    "kids_what_we_noticed": "#### Ce que nous avons remarqué",
    "kids_answer_prompt": "Réponds à quelques questions ci-dessus pour voir le résumé de ton bilan.",
    "kids_steady": (
        "D'après tes réponses, les choses semblent plutôt stables en ce moment. C'est "
        "excellent — et c'est toujours bien de parler à quelqu'un de confiance si ça change."
    ),
    "kids_learn_more": "En savoir plus",
    "kids_resources_header": "#### Ressources pour toi",
    "kids_footer_note": (
        "Ce bilan n'est pas un diagnostic et ne remplace pas une vraie conversation avec une "
        "personne. Un parent, un proche, un enseignant, un conseiller scolaire ou un médecin "
        "peut t'aider à décider quoi faire ensuite."
    ),
    "answer_not_really": "Pas vraiment",
    "answer_sometimes": "Parfois",
    "answer_a_lot": "Beaucoup",
    "checker_disclaimer_title": "⚠️ Avertissement important — à lire",
    "checker_disclaimer_body": (
        "Cet outil est **à des fins éducatives uniquement** et ne fournit pas de conseils, de "
        "diagnostic ou de traitement médical ou de santé mentale. Il utilise une simple "
        "correspondance de symptômes, pas un modèle clinique ou d'IA. Consultez toujours un "
        "médecin ou un professionnel de la santé mentale qualifié pour tout problème de santé. "
        "Si vous pensez être en situation d'urgence médicale ou de santé mentale, contactez "
        "immédiatement les services d'urgence locaux."
    ),
    "checker_step1": "1. Sélectionnez vos symptômes",
    "checker_multiselect_label": "Commencez à taper pour rechercher, ou faites défiler pour parcourir. Sélectionnez tout ce qui s'applique.",
    "checker_multiselect_placeholder": "🔍  ex. tristesse persistante, mal de tête, essoufflement...",
    "checker_analyze_button": "Analyser les symptômes",
    "checker_emergency_title": "### 🚨 Cela pourrait être une urgence médicale",
    "checker_emergency_seek_help": "**Cherchez de l'aide immédiatement. Ressources de crise et d'urgence :**",
    "checker_step2": "2. Correspondances possibles",
    "checker_select_prompt": "Sélectionnez un ou plusieurs symptômes ci-dessus, puis cliquez sur **Analyser les symptômes**.",
    "checker_no_matches": "Aucune affection correspondante trouvée pour les symptômes sélectionnés dans cet ensemble de référence.",
    "checker_category_label": "Catégorie : {category}",
    "checker_match_score": "Score de correspondance : {pct} %",
    "checker_matched_symptoms": "✅ **Symptômes correspondants :** {symptoms}",
    "checker_missing_symptoms": "ℹ️ **Autres symptômes typiques non sélectionnés :** {symptoms}",
    "checker_suggested_next_step": "**Prochaine étape suggérée :** {advice}",
    "checker_mayo_expander": "📖 Résumé IA de la Mayo Clinic",
    "checker_mayo_source": "Source : [Mayo Clinic]({url})",
    "checker_footer_note": (
        "Les résultats sont classés uniquement selon la correspondance des symptômes et peuvent "
        "inclure des affections qui ne vous concernent pas. Ce n'est pas un diagnostic — "
        "consultez un professionnel de santé pour confirmer toute affection."
    ),
    "tab_mental_health": "🧠 Bilan de santé mentale",
    "mh_subheader": "Un moment pour votre santé mentale",
    "mh_caption": (
        "Un bilan bref et privé inspiré de questionnaires de dépistage clinique largement "
        "utilisés (PHQ-9 pour l'humeur, GAD-7 pour l'anxiété). Ce n'est pas un diagnostic — "
        "juste une façon de remarquer des tendances qui méritent d'être abordées avec un "
        "professionnel."
    ),
    "mh_disclaimer_title": "⚠️ Avertissement important — à lire",
    "mh_disclaimer_body": (
        "Ce bilan est **à des fins éducatives et d'introspection uniquement**. Il s'inspire "
        "de questionnaires de dépistage standards utilisés en contexte clinique, mais y "
        "répondre ici ne diagnostique aucune condition. Seul un professionnel de la santé "
        "mentale qualifié peut poser un diagnostic. Si vous êtes en crise ou pensez à vous "
        "faire du mal, contactez immédiatement les ressources ci-dessous."
    ),
    "mh_depression_header": "Au cours des 2 dernières semaines, à quelle fréquence avez-vous été gêné(e) par les éléments suivants ?",
    "mh_anxiety_header": "Et à quelle fréquence avez-vous été gêné(e) par ceci ?",
    "mh_one_more_question": (
        "**Une dernière question.** Celle-ci concerne simplement votre sécurité — c'est "
        "toujours bien de répondre honnêtement."
    ),
    "mh_submit_button": "Voir mes résultats",
    "mh_safety_alert_body": (
        "Merci d'avoir été honnête — cela demande du courage. Contactez immédiatement l'une "
        "des ressources ci-dessous, ou une personne de confiance :"
    ),
    "mh_prompt": "Répondez aux questions ci-dessus, puis cliquez sur **Voir mes résultats**.",
    "mh_results_header": "#### Résultats de votre bilan",
    "mh_depression_result": "Indicateur de dépression : **{label}** ({score}/27)",
    "mh_anxiety_result": "Indicateur d'anxiété : **{label}** ({score}/12)",
    "mh_results_note": (
        "Ce ne sont que des indicateurs de dépistage, inspirés de questionnaires cliniques "
        "standards — pas un diagnostic. Un professionnel de la santé mentale peut vous "
        "fournir une véritable évaluation et discuter de ce que ces tendances pourraient "
        "signifier pour vous."
    ),
    "mh_learn_more_depression": "📖 En savoir plus sur la dépression",
    "mh_learn_more_anxiety": "📖 En savoir plus sur l'anxiété",
    "mh_resources_header": "#### Ressources",
    "mh_footer_note": (
        "Ce bilan ne remplace pas une conversation avec un professionnel de la santé mentale "
        "agréé. Si quelque chose ici vous préoccupe, n'hésitez pas à demander du soutien."
    ),
    "tab_games": "🧘 Jeux et respiration",
    "games_subheader": "Prenez un moment pour respirer",
    "games_caption": (
        "Quelques outils simples et non cliniques pour soulager le stress : respiration "
        "guidée, un exercice d'ancrage, un jeu de bulles anti-stress, un bocal de "
        "gratitude et des affirmations bienveillantes. Ce n'est pas un traitement et cela "
        "ne remplace pas les soins professionnels."
    ),
    "games_breathing_header": "🌬️ Respiration guidée",
    "games_breathing_select_label": "Choisissez un rythme de respiration",
    "games_breathing_hint": "Suivez le cercle : il grandit à l'inspiration, se maintient, se réduit à l'expiration, se maintient.",
    "games_phase_inhale": "Inspirez",
    "games_phase_hold": "Retenez",
    "games_phase_exhale": "Expirez",
    "games_grounding_header": "🌳 Exercice d'ancrage 5-4-3-2-1",
    "games_grounding_caption": (
        "Une technique d'ancrage classique pour apaiser un esprit agité en observant votre "
        "environnement à travers vos sens."
    ),
    "games_grounding_complete": "Bien joué, vous vous êtes ancré dans le moment présent. 🌿",
    "games_bubbles_header": "🫧 Bulles anti-stress",
    "games_bubbles_caption": "Un petit jeu pour les mains — éclatez quelques bulles pour évacuer la tension.",
    "games_bubbles_counter": "Éclatées : {popped} / {total}",
    "games_bubbles_reset": "Remplir les bulles",
    "games_gratitude_header": "📝 Bocal de gratitude",
    "games_gratitude_caption": "Notez quelques petites choses pour lesquelles vous êtes reconnaissant aujourd'hui.",
    "games_gratitude_placeholder": "Quelque chose pour lequel vous êtes reconnaissant...",
    "games_gratitude_add": "Ajouter au bocal",
    "games_gratitude_clear": "Vider le bocal",
    "games_gratitude_empty": "Votre bocal est vide — ajoutez quelque chose de petit et de bon aujourd'hui.",
    "games_affirmation_header": "💛 Affirmations bienveillantes",
    "games_affirmation_caption": "Un petit rappel, quand vous en avez besoin.",
    "games_affirmation_button": "Montrez-moi une affirmation",
    "games_footer_note": (
        "Ce sont de simples outils de relaxation, pas une thérapie ni un traitement "
        "médical. Si vous traversez une période difficile, l'onglet Bilan de santé "
        "mentale propose des ressources, dont la ligne 988 Suicide & Crisis Lifeline."
    ),
    "assistant_subheader": "Posez une question",
    "assistant_caption": (
        "Un assistant IA compétent en santé, ancré dans les propres données sur les affections "
        "de cette application — plus tout contenu supplémentaire chargé dans la base de "
        "connaissances (voir l'onglet Téléverser des documents) — et soutenu par des "
        "connaissances médicales et de santé mentale générales pour le reste. Ce n'est pas un "
        "diagnostic et cela ne remplace pas une vraie conversation avec un professionnel qualifié."
    ),
    "assistant_not_configured": (
        "L'Assistant IA n'est pas encore configuré. Ajoutez `ANTHROPIC_API_KEY` à "
        "`.streamlit/secrets.toml` — voir `.streamlit/secrets.toml.example` pour la configuration."
    ),
    "assistant_preparing_kb": "Préparation de la base de connaissances...",
    "assistant_chat_placeholder": "Posez une question de santé...",
    "assistant_crisis_answer": (
        "J'ai remarqué que votre question pourrait concerner des pensées d'automutilation ou "
        "une crise. Merci de contacter immédiatement les ressources ci-dessus — une vraie "
        "personne peut vous aider d'une façon que je ne peux pas."
    ),
    "assistant_thinking": "Réflexion...",
    "assistant_error_prefix": "Un problème est survenu en répondant à cela : {error}",
    "assistant_sources_prefix": "Sources : {sources}",
    "upload_subheader": "Charger un document dans la base de connaissances",
    "upload_caption": (
        "Les documents téléversés ici sont partagés avec l'Assistant IA de tous les visiteurs — "
        "ils sont ajoutés à une base de connaissances, pas gardés privés à votre session."
    ),
    "upload_not_configured": (
        "Le téléversement de documents n'est pas encore configuré. Ajoutez `ANTHROPIC_API_KEY` à "
        "`.streamlit/secrets.toml` — voir `.streamlit/secrets.toml.example` pour la configuration."
    ),
    "upload_kb_stats": "La base de connaissances contient actuellement **{chunks}** extraits de **{documents}** document(s).",
    "upload_set_password": "Définissez `ADMIN_PASSWORD` dans les secrets pour activer le téléversement de documents.",
    "upload_password_label": "Mot de passe administrateur",
    "upload_file_uploader_label": "Téléversez des fichiers .txt, .md ou .pdf",
    "upload_add_button": "Ajouter à la base de connaissances",
    "upload_processing": "Traitement de {filename}...",
    "upload_error": "Impossible d'ajouter {filename} : {error}",
    "upload_success": "{filename} ajouté ({count} extraits).",
    "upload_incorrect_password": "Mot de passe incorrect.",
    "hospital_subheader": "Trouver un hôpital à proximité",
    "hospital_caption": (
        "Cliquez sur « Utiliser ma position » ou entrez une ville/adresse pour voir les hôpitaux "
        "à proximité sur une carte gratuite, avec les données OpenStreetMap — aucun compte ni "
        "clé API nécessaire. **S'il s'agit d'une véritable urgence, appelez votre numéro "
        "d'urgence local (ex. 911/112/999) au lieu d'attendre sur cette page.**"
    ),
    "hospital_use_location_button": "📍 Utiliser ma position",
    "hospital_manual_location_label": "Ou entrez une ville, une adresse ou un code postal",
    "hospital_manual_location_placeholder": "ex. Boston, MA",
    "hospital_search_button": "Rechercher cette position",
    "hospital_radius_label": "Rayon de recherche (km)",
    "hospital_getting_location": "Obtention de votre position...",
    "hospital_geo_error": (
        "Impossible d'obtenir votre position ({error}). Autorisez l'accès à la position dans "
        "votre navigateur, ou recherchez par adresse à la place."
    ),
    "hospital_your_location_label": "votre position actuelle",
    "hospital_looking_up": "Recherche de cette position...",
    "hospital_geocode_service_error": (
        "Impossible de contacter le service de localisation. Vérifiez votre connexion internet "
        "et réessayez."
    ),
    "hospital_not_found": "Impossible de trouver cette position. Essayez une adresse ou une ville plus précise.",
    "hospital_searching": "Recherche d'hôpitaux à proximité...",
    "hospital_search_service_error": (
        "Impossible de contacter le service de recherche d'hôpitaux. Vérifiez votre connexion "
        "internet et réessayez."
    ),
    "hospital_showing_results": "📍 Résultats affichés près de **{location}**",
    "hospital_no_results": "Aucun hôpital trouvé dans ce rayon. Essayez d'augmenter le rayon de recherche.",
    "hospital_distance_away": "**à {distance} km**",
    "hospital_has_er": "🚨 **Dispose d'un service d'urgences**",
    "hospital_get_directions": "[Obtenir l'itinéraire ↗]({url})",
    "hospital_prompt": "Cliquez sur **Utiliser ma position** ou recherchez une adresse pour voir les hôpitaux à proximité.",
}

UI_STRINGS["hi"] = {
    "language_label": "🌐 भाषा",
    "app_caption": (
        "बच्चों और किशोरों के लिए एक सहयोगी चेक-इन, साथ ही शारीरिक और मानसिक स्वास्थ्य के लक्षणों की "
        "तुलना के लिए एक नियम-आधारित उपकरण। दोनों में से कोई भी निदान नहीं है।"
    ),
    "breadcrumb": "होम &nbsp;›&nbsp; बीमारियाँ और स्थितियाँ &nbsp;›&nbsp; लक्षण और कल्याण जाँचकर्ता",
    "topbar": "🩺&nbsp; लक्षण और कल्याण जाँचकर्ता",
    "hero_explore_label": "इस ऐप को देखें",
    "footer": (
        "शैक्षिक/हैकाथॉन उद्देश्यों के लिए बनाया गया। वास्तविक निदान और उपचार के लिए हमेशा एक लाइसेंस "
        "प्राप्त चिकित्सा या मानसिक स्वास्थ्य पेशेवर से सलाह लें।"
    ),
    "translation_fallback_note": (
        "🌐 इस सामग्री के पूर्ण अनुवाद के लिए AI सहायक को कॉन्फ़िगर करना आवश्यक है (AI सहायक टैब देखें) "
        "— फिलहाल अंग्रेज़ी दिखाई जा रही है।"
    ),
    "sidebar_filters_header": "फ़िल्टर",
    "sidebar_filters_caption": "लक्षण जाँचकर्ता टैब पर लागू होता है।",
    "sidebar_categories_label": "आप कौन से क्षेत्र जाँचना चाहते हैं?",
    "sidebar_select_category_warning": "जारी रखने के लिए कम से कम एक श्रेणी चुनें।",
    "sidebar_about_header": "इसके बारे में",
    "sidebar_about_text": (
        "यह जाँचकर्ता आपके चुने हुए लक्षणों की तुलना **{total} स्थितियों** ({physical} शारीरिक, "
        "{mental} मानसिक स्वास्थ्य) की एक क्यूरेटेड सूची से करता है और यह देखता है कि आपके लक्षण हर "
        "स्थिति की सामान्य प्रोफ़ाइल से कितनी अच्छी तरह मेल खाते हैं।"
    ),
    "tab_kids": "🧒 बच्चों और किशोरों की जाँच",
    "tab_checker": "🔍 लक्षण जाँचकर्ता",
    "tab_assistant": "🤖 AI सहायक",
    "tab_upload": "📄 दस्तावेज़ अपलोड करें",
    "tab_hospital": "🏥 अस्पताल खोजें",
    "kids_subheader": "एक त्वरित, मित्रवत जाँच",
    "kids_caption": (
        "यह कोई परीक्षा, स्कोर या निदान नहीं है — बस कुछ सवाल हैं जो यह जानने में मदद करते हैं कि आप "
        "हाल ही में कैसा महसूस कर रहे हैं। ईमानदारी से उत्तर दें। यहाँ कुछ भी आँका नहीं जाता, और आपके "
        "उत्तर कहीं भी सहेजे नहीं जाते।"
    ),
    "kids_one_more_question": (
        "**एक और सवाल।** यह सिर्फ़ आपकी सुरक्षा के बारे में है — ईमानदारी से जवाब देना हमेशा ठीक है।"
    ),
    "kids_submit_button": "देखें इसका क्या मतलब हो सकता है",
    "kids_safety_alert_title": "💙 अभी आपकी सुरक्षा सबसे ज़्यादा मायने रखती है",
    "kids_safety_alert_body": (
        "ईमानदार होने के लिए धन्यवाद — इसके लिए हिम्मत चाहिए। कृपया तुरंत किसी भरोसेमंद बड़े व्यक्ति "
        "को बताएँ (माता-पिता, रिश्तेदार, शिक्षक, या स्कूल काउंसलर), या अभी संपर्क करें:"
    ),
    "kids_988_line": (
        "**[988 सुसाइड एंड क्राइसिस लाइफलाइन](https://988lifeline.org/)**: 988 पर कॉल या टेक्स्ट करें "
        "— मुफ़्त, गोपनीय, 24/7।"
    ),
    "kids_crisis_text_line": (
        "**[क्राइसिस टेक्स्ट लाइन](https://www.crisistextline.org/)**: 741741 पर HOME लिखकर भेजें "
        "— मुफ़्त, 24/7।"
    ),
    "kids_what_we_noticed": "#### हमने क्या देखा",
    "kids_answer_prompt": "अपना चेक-इन सारांश देखने के लिए ऊपर कुछ सवालों के जवाब दें।",
    "kids_steady": (
        "आपके जवाबों के आधार पर, अभी चीज़ें काफ़ी स्थिर लग रही हैं। यह बहुत अच्छा है — और अगर यह "
        "बदल जाए तो किसी भरोसेमंद व्यक्ति से बात करना हमेशा ठीक है।"
    ),
    "kids_learn_more": "और जानें",
    "kids_resources_header": "#### आपके लिए संसाधन",
    "kids_footer_note": (
        "यह जाँच कोई निदान नहीं है और किसी वास्तविक व्यक्ति से बात करने का विकल्प नहीं है। एक "
        "माता-पिता, रिश्तेदार, शिक्षक, स्कूल काउंसलर, या डॉक्टर यह तय करने में आपकी मदद कर सकते हैं "
        "कि आगे क्या करना है।"
    ),
    "answer_not_really": "ऐसा नहीं",
    "answer_sometimes": "कभी-कभी",
    "answer_a_lot": "बहुत ज़्यादा",
    "checker_disclaimer_title": "⚠️ महत्वपूर्ण अस्वीकरण — कृपया पढ़ें",
    "checker_disclaimer_body": (
        "यह उपकरण **केवल शैक्षिक उद्देश्यों** के लिए है और यह चिकित्सा या मानसिक स्वास्थ्य सलाह, निदान, "
        "या उपचार प्रदान नहीं करता। यह एक सरल लक्षण मिलान का उपयोग करता है, न कि किसी क्लिनिकल या "
        "AI मॉडल का। किसी भी स्वास्थ्य संबंधी चिंता के लिए हमेशा एक योग्य डॉक्टर या मानसिक स्वास्थ्य "
        "पेशेवर से सलाह लें। यदि आपको लगता है कि आप किसी चिकित्सा या मानसिक स्वास्थ्य आपातकाल का "
        "सामना कर रहे हैं, तो तुरंत अपनी स्थानीय आपातकालीन सेवाओं से संपर्क करें।"
    ),
    "checker_step1": "1. अपने लक्षण चुनें",
    "checker_multiselect_label": "खोजने के लिए टाइप करना शुरू करें, या ब्राउज़ करने के लिए स्क्रॉल करें। जो भी लागू हो उसे चुनें।",
    "checker_multiselect_placeholder": "🔍  जैसे लगातार उदासी, सिरदर्द, सांस लेने में तकलीफ़...",
    "checker_analyze_button": "लक्षणों का विश्लेषण करें",
    "checker_emergency_title": "### 🚨 यह एक चिकित्सा आपातकाल हो सकता है",
    "checker_emergency_seek_help": "**कृपया तुरंत मदद लें। संकट और आपातकालीन संसाधन:**",
    "checker_step2": "2. संभावित मिलान",
    "checker_select_prompt": "ऊपर एक या अधिक लक्षण चुनें, फिर **लक्षणों का विश्लेषण करें** पर क्लिक करें।",
    "checker_no_matches": "इस संदर्भ सेट में चुने गए लक्षणों से मेल खाने वाली कोई स्थिति नहीं मिली।",
    "checker_category_label": "श्रेणी: {category}",
    "checker_match_score": "मिलान स्कोर: {pct}%",
    "checker_matched_symptoms": "✅ **मेल खाने वाले लक्षण:** {symptoms}",
    "checker_missing_symptoms": "ℹ️ **अन्य सामान्य लक्षण जो नहीं चुने गए:** {symptoms}",
    "checker_suggested_next_step": "**सुझाया गया अगला कदम:** {advice}",
    "checker_mayo_expander": "📖 Mayo Clinic का AI सारांश",
    "checker_mayo_source": "स्रोत: [Mayo Clinic]({url})",
    "checker_footer_note": (
        "परिणाम केवल लक्षण मिलान के आधार पर क्रमबद्ध किए गए हैं और इसमें ऐसी स्थितियाँ भी शामिल हो "
        "सकती हैं जो आप पर लागू न हों। यह कोई निदान नहीं है — किसी भी स्थिति की पुष्टि के लिए कृपया "
        "किसी स्वास्थ्य पेशेवर से सलाह लें।"
    ),
    "tab_mental_health": "🧠 मानसिक स्वास्थ्य जाँच",
    "mh_subheader": "आपके मानसिक स्वास्थ्य के लिए एक पल",
    "mh_caption": (
        "व्यापक रूप से उपयोग की जाने वाली नैदानिक स्क्रीनिंग प्रश्नावली (मनोदशा के लिए PHQ-9, चिंता के "
        "लिए GAD-7) से प्रेरित एक संक्षिप्त, निजी स्व-जाँच। यह निदान नहीं है — बस उन पैटर्न को नोटिस "
        "करने का एक तरीका है जिनके बारे में किसी पेशेवर से बात करना उचित हो सकता है।"
    ),
    "mh_disclaimer_title": "⚠️ महत्वपूर्ण अस्वीकरण — कृपया पढ़ें",
    "mh_disclaimer_body": (
        "यह जाँच केवल **शैक्षिक और आत्म-चिंतन उद्देश्यों** के लिए है। यह क्लिनिकल सेटिंग्स में उपयोग "
        "की जाने वाली मानक स्क्रीनिंग प्रश्नावली से प्रेरित है, लेकिन यहाँ इसका उत्तर देने से किसी "
        "स्थिति का निदान नहीं होता। केवल एक योग्य मानसिक स्वास्थ्य पेशेवर ही निदान कर सकता है। यदि "
        "आप संकट में हैं या स्वयं को नुकसान पहुँचाने के बारे में सोच रहे हैं, तो कृपया तुरंत नीचे दिए "
        "गए संसाधनों से संपर्क करें।"
    ),
    "mh_depression_header": "पिछले 2 हफ्तों में, आप निम्नलिखित में से किसी से कितनी बार परेशान हुए हैं?",
    "mh_anxiety_header": "और आप इनसे कितनी बार परेशान हुए हैं?",
    "mh_one_more_question": (
        "**एक और सवाल।** यह सिर्फ़ आपकी सुरक्षा के बारे में है — ईमानदारी से जवाब देना हमेशा ठीक है।"
    ),
    "mh_submit_button": "मेरे परिणाम देखें",
    "mh_safety_alert_body": (
        "ईमानदार होने के लिए धन्यवाद — इसके लिए हिम्मत चाहिए। कृपया अभी नीचे दिए गए संसाधनों में से "
        "किसी एक से संपर्क करें, या किसी भरोसेमंद व्यक्ति से बात करें:"
    ),
    "mh_prompt": "ऊपर दिए गए सवालों के जवाब दें, फिर **मेरे परिणाम देखें** पर क्लिक करें।",
    "mh_results_header": "#### आपकी जाँच के परिणाम",
    "mh_depression_result": "अवसाद संकेतक: **{label}** ({score}/27)",
    "mh_anxiety_result": "चिंता संकेतक: **{label}** ({score}/12)",
    "mh_results_note": (
        "ये केवल स्क्रीनिंग संकेतक हैं, मानक क्लिनिकल प्रश्नावली से प्रेरित — निदान नहीं। एक मानसिक "
        "स्वास्थ्य पेशेवर आपको एक वास्तविक मूल्यांकन दे सकता है और चर्चा कर सकता है कि ये पैटर्न आपके "
        "लिए क्या मायने रख सकते हैं।"
    ),
    "mh_learn_more_depression": "📖 अवसाद के बारे में और जानें",
    "mh_learn_more_anxiety": "📖 चिंता के बारे में और जानें",
    "mh_resources_header": "#### संसाधन",
    "mh_footer_note": (
        "यह जाँच किसी लाइसेंस प्राप्त मानसिक स्वास्थ्य पेशेवर के साथ बातचीत का विकल्प नहीं है। यदि "
        "यहाँ कुछ भी आपको चिंतित करता है, तो कृपया सहायता लें।"
    ),
    "tab_games": "🧘 खेल और श्वास अभ्यास",
    "games_subheader": "थोड़ी सांस लें",
    "games_caption": (
        "तनाव कम करने के लिए कुछ सरल, गैर-चिकित्सीय उपकरण — निर्देशित श्वास, एक ग्राउंडिंग "
        "अभ्यास, तनाव-मुक्ति के लिए बबल पॉप गेम, एक आभार जार, और सौम्य पुष्टिकरण। यह उपचार "
        "नहीं है और पेशेवर देखभाल का विकल्प नहीं है।"
    ),
    "games_breathing_header": "🌬️ निर्देशित श्वास",
    "games_breathing_select_label": "एक श्वास पैटर्न चुनें",
    "games_breathing_hint": "वृत्त का अनुसरण करें: सांस लेते समय बड़ा हो, रुके, सांस छोड़ते समय छोटा हो, फिर रुके।",
    "games_phase_inhale": "सांस लें",
    "games_phase_hold": "रोकें",
    "games_phase_exhale": "सांस छोड़ें",
    "games_grounding_header": "🌳 5-4-3-2-1 ग्राउंडिंग अभ्यास",
    "games_grounding_caption": (
        "अपनी इंद्रियों के माध्यम से अपने आस-पास को महसूस करके व्यस्त मन को शांत करने की एक "
        "पारंपरिक ग्राउंडिंग तकनीक।"
    ),
    "games_grounding_complete": "वर्तमान क्षण में खुद को स्थिर करने के लिए बढ़िया काम। 🌿",
    "games_bubbles_header": "🫧 बबल पॉप",
    "games_bubbles_caption": "एक छोटा सा फिजेट खिलौना — तनाव दूर करने के लिए कुछ बबल पॉप करें।",
    "games_bubbles_counter": "फोड़े गए: {popped} / {total}",
    "games_bubbles_reset": "बबल फिर से भरें",
    "games_gratitude_header": "📝 आभार जार",
    "games_gratitude_caption": "आज आप जिन छोटी-छोटी बातों के लिए आभारी हैं, उन्हें लिखें।",
    "games_gratitude_placeholder": "कुछ ऐसा जिसके लिए आप आभारी हैं...",
    "games_gratitude_add": "जार में जोड़ें",
    "games_gratitude_clear": "जार खाली करें",
    "games_gratitude_empty": "आपका जार खाली है — आज की कोई छोटी और अच्छी बात जोड़ें।",
    "games_affirmation_header": "💛 सौम्य पुष्टिकरण",
    "games_affirmation_caption": "जब भी आपको ज़रूरत हो, एक छोटी याद दिलाने वाली बात।",
    "games_affirmation_button": "मुझे एक पुष्टिकरण दिखाएँ",
    "games_footer_note": (
        "ये सरल विश्राम उपकरण हैं, चिकित्सा या उपचार नहीं। यदि आप कठिनाई महसूस कर रहे हैं, तो "
        "मानसिक स्वास्थ्य जाँच टैब में 988 सुसाइड एंड क्राइसिस लाइफ़लाइन सहित संसाधन उपलब्ध हैं।"
    ),
    "assistant_subheader": "एक सवाल पूछें",
    "assistant_caption": (
        "इस ऐप के अपने स्थिति डेटा पर आधारित एक स्वास्थ्य-कुशल AI सहायक — साथ ही नॉलेज बेस में लोड "
        "किया गया कोई भी अतिरिक्त कंटेंट (दस्तावेज़ अपलोड करें टैब देखें) — और बाकी सब के लिए सामान्य "
        "चिकित्सा/मानसिक स्वास्थ्य ज्ञान द्वारा समर्थित। यह कोई निदान नहीं है और किसी योग्य पेशेवर के "
        "साथ वास्तविक बातचीत का विकल्प नहीं है।"
    ),
    "assistant_not_configured": (
        "AI सहायक अभी सेट अप नहीं हुआ है। `.streamlit/secrets.toml` में `ANTHROPIC_API_KEY` जोड़ें "
        "— सेटअप के लिए `.streamlit/secrets.toml.example` देखें।"
    ),
    "assistant_preparing_kb": "नॉलेज बेस तैयार किया जा रहा है...",
    "assistant_chat_placeholder": "एक स्वास्थ्य सवाल पूछें...",
    "assistant_crisis_answer": (
        "मैंने देखा कि आपके सवाल में आत्म-हानि या संकट के विचार शामिल हो सकते हैं। कृपया ऊपर दिए गए "
        "संसाधनों से तुरंत संपर्क करें — एक वास्तविक व्यक्ति उस तरह से मदद कर सकता है जैसे मैं नहीं कर सकता।"
    ),
    "assistant_thinking": "सोच रहा हूँ...",
    "assistant_error_prefix": "उसका उत्तर देने में कुछ गड़बड़ हो गई: {error}",
    "assistant_sources_prefix": "स्रोत: {sources}",
    "upload_subheader": "नॉलेज बेस में एक दस्तावेज़ लोड करें",
    "upload_caption": (
        "यहाँ अपलोड किए गए दस्तावेज़ हर विज़िटर के AI सहायक के साथ साझा किए जाते हैं — वे एक नॉलेज "
        "बेस में जोड़े जाते हैं, आपके सत्र के लिए निजी नहीं रखे जाते।"
    ),
    "upload_not_configured": (
        "दस्तावेज़ अपलोड अभी सेट अप नहीं हुआ है। `.streamlit/secrets.toml` में `ANTHROPIC_API_KEY` "
        "जोड़ें — सेटअप के लिए `.streamlit/secrets.toml.example` देखें।"
    ),
    "upload_kb_stats": "नॉलेज बेस में अभी **{documents}** दस्तावेज़ों से **{chunks}** हिस्से हैं।",
    "upload_set_password": "दस्तावेज़ अपलोड सक्षम करने के लिए secrets में `ADMIN_PASSWORD` सेट करें।",
    "upload_password_label": "एडमिन पासवर्ड",
    "upload_file_uploader_label": ".txt, .md, या .pdf फ़ाइलें अपलोड करें",
    "upload_add_button": "नॉलेज बेस में जोड़ें",
    "upload_processing": "{filename} प्रोसेस हो रहा है...",
    "upload_error": "{filename} नहीं जोड़ा जा सका: {error}",
    "upload_success": "{filename} जोड़ा गया ({count} हिस्से)।",
    "upload_incorrect_password": "गलत पासवर्ड।",
    "hospital_subheader": "पास का अस्पताल खोजें",
    "hospital_caption": (
        "पास के अस्पतालों को एक मुफ़्त मानचित्र पर देखने के लिए \"मेरा स्थान उपयोग करें\" पर क्लिक करें या "
        "कोई शहर/पता दर्ज करें, OpenStreetMap डेटा का उपयोग करते हुए — किसी खाते या API कुंजी की "
        "आवश्यकता नहीं। **यदि यह वास्तविक आपातकाल है, तो इस पेज पर इंतज़ार करने के बजाय अपने "
        "स्थानीय आपातकालीन नंबर पर कॉल करें (जैसे 911/112/999)।**"
    ),
    "hospital_use_location_button": "📍 मेरा स्थान उपयोग करें",
    "hospital_manual_location_label": "या कोई शहर, पता, या पिन कोड दर्ज करें",
    "hospital_manual_location_placeholder": "जैसे Boston, MA",
    "hospital_search_button": "यह स्थान खोजें",
    "hospital_radius_label": "खोज त्रिज्या (किमी)",
    "hospital_getting_location": "आपका स्थान प्राप्त किया जा रहा है...",
    "hospital_geo_error": (
        "आपका स्थान प्राप्त नहीं हो सका ({error})। अपने ब्राउज़र में स्थान की पहुँच की अनुमति दें, या "
        "इसके बजाय पते से खोजें।"
    ),
    "hospital_your_location_label": "आपका वर्तमान स्थान",
    "hospital_looking_up": "वह स्थान खोजा जा रहा है...",
    "hospital_geocode_service_error": (
        "स्थान सेवा तक नहीं पहुँचा जा सका। अपना इंटरनेट कनेक्शन जाँचें और फिर से प्रयास करें।"
    ),
    "hospital_not_found": "वह स्थान नहीं मिला। कृपया अधिक सटीक पता या शहर आज़माएँ।",
    "hospital_searching": "पास के अस्पताल खोजे जा रहे हैं...",
    "hospital_search_service_error": (
        "अस्पताल खोज सेवा तक नहीं पहुँचा जा सका। अपना इंटरनेट कनेक्शन जाँचें और फिर से प्रयास करें।"
    ),
    "hospital_showing_results": "📍 **{location}** के पास के परिणाम दिखाए जा रहे हैं",
    "hospital_no_results": "इस त्रिज्या में कोई अस्पताल नहीं मिला। खोज त्रिज्या बढ़ाने का प्रयास करें।",
    "hospital_distance_away": "**{distance} किमी दूर**",
    "hospital_has_er": "🚨 **आपातकालीन विभाग है**",
    "hospital_get_directions": "[दिशा-निर्देश पाएँ ↗]({url})",
    "hospital_prompt": "पास के अस्पताल देखने के लिए **मेरा स्थान उपयोग करें** पर क्लिक करें या कोई पता खोजें।",
}


# Translated "detail" text for kids_data.KIDS_RESOURCES, in the same order.
# Labels and URLs stay in English/unchanged (organization names + external
# links that are themselves in English).
KIDS_RESOURCE_DETAILS_I18N = {
    "en": [
        "Call or text 988 — free, confidential, 24/7. For any crisis, not just suicide.",
        "Text HOME to 741741 — free, 24/7 support by text.",
        "Call 1-800-950-6264, text \"Friend\" to 62640, or chat at nami.org/talktous. Mon–Fri, "
        "10am–10pm ET. Free peer support — not a crisis line (use 988 for a crisis).",
        "Call 1-800-662-HELP (4357), 24/7/365, free and confidential, English & Spanish. "
        "Treatment referrals for mental health and substance use.",
        "A free, anonymous screening tool for ages 11-17 to check in on emotions, attention, or behavior.",
        "Clear, research-based information for kids, teens, and families.",
    ],
    "es": [
        "Llama o envía un mensaje al 988 — gratis, confidencial, 24/7. Para cualquier crisis, no solo suicidio.",
        "Envía HOME al 741741 — apoyo gratuito por mensaje de texto, 24/7.",
        "Llama al 1-800-950-6264, envía \"Friend\" al 62640, o chatea en nami.org/talktous. Lun–vie, "
        "10am–10pm ET. Apoyo gratuito entre pares — no es una línea de crisis (usa el 988 para una crisis).",
        "Llama al 1-800-662-HELP (4357), 24/7/365, gratis y confidencial, en inglés y español. "
        "Referencias de tratamiento para salud mental y uso de sustancias.",
        "Una herramienta de evaluación gratuita y anónima para edades de 11 a 17 años para revisar "
        "emociones, atención o comportamiento.",
        "Información clara y basada en investigación para niños, adolescentes y familias.",
    ],
    "fr": [
        "Appelez ou envoyez un SMS au 988 — gratuit, confidentiel, 24/7. Pour toute crise, pas "
        "seulement le suicide.",
        "Envoyez HOME au 741741 — soutien gratuit par SMS, 24/7.",
        "Appelez le 1-800-950-6264, envoyez « Friend » au 62640, ou discutez sur nami.org/talktous. "
        "Lun–ven, 10h–22h (heure de l'Est). Soutien gratuit par des pairs — ce n'est pas une ligne "
        "de crise (utilisez le 988 en cas de crise).",
        "Appelez le 1-800-662-HELP (4357), 24/7/365, gratuit et confidentiel, en anglais et espagnol. "
        "Orientation vers des traitements pour la santé mentale et les dépendances.",
        "Un outil de dépistage gratuit et anonyme pour les 11-17 ans, pour faire le point sur les "
        "émotions, l'attention ou le comportement.",
        "Des informations claires et fondées sur la recherche pour les enfants, les adolescents et "
        "les familles.",
    ],
    "hi": [
        "988 पर कॉल या टेक्स्ट करें — मुफ़्त, गोपनीय, 24/7। किसी भी संकट के लिए, केवल आत्महत्या के लिए नहीं।",
        "741741 पर HOME लिखकर भेजें — मुफ़्त, 24/7 टेक्स्ट सहायता।",
        "1-800-950-6264 पर कॉल करें, 62640 पर \"Friend\" लिखकर भेजें, या nami.org/talktous पर चैट करें। "
        "सोम–शुक्र, सुबह 10 से रात 10 बजे (ET)। मुफ़्त पीयर सहायता — यह क्राइसिस लाइन नहीं है (संकट के लिए 988 का उपयोग करें)।",
        "1-800-662-HELP (4357) पर कॉल करें, 24/7/365, मुफ़्त और गोपनीय, अंग्रेज़ी और स्पैनिश में। मानसिक "
        "स्वास्थ्य और नशे से जुड़े उपचार के लिए रेफ़रल।",
        "11-17 वर्ष के लिए भावनाओं, ध्यान, या व्यवहार की जाँच हेतु एक मुफ़्त, गुमनाम स्क्रीनिंग उपकरण।",
        "बच्चों, किशोरों, और परिवारों के लिए स्पष्ट, शोध-आधारित जानकारी।",
    ],
}

# Translated "detail" text for mental_health_data.MENTAL_HEALTH_RESOURCES, in
# the same order. Labels and URLs stay in English/unchanged.
MENTAL_HEALTH_RESOURCE_DETAILS_I18N = {
    "en": [
        "Call or text 988 — free, confidential, 24/7.",
        "Text HOME to 741741 — free, 24/7 support by text.",
        "Call 1-800-950-6264 or text \"HelpLine\" to 62640. Mon-Fri, 10am-10pm ET. Free peer "
        "support and referrals — not a crisis line (use 988 for a crisis).",
        "Call 1-800-662-HELP (4357), 24/7/365, free and confidential, English & Spanish. "
        "Treatment referrals for mental health and substance use.",
    ],
    "es": [
        "Llama o envía un mensaje al 988 — gratis, confidencial, 24/7.",
        "Envía HOME al 741741 — apoyo gratuito por mensaje de texto, 24/7.",
        "Llama al 1-800-950-6264 o envía \"HelpLine\" al 62640. Lun-vie, 10am-10pm ET. Apoyo "
        "gratuito entre pares y referencias — no es una línea de crisis (usa el 988 para una "
        "crisis).",
        "Llama al 1-800-662-HELP (4357), 24/7/365, gratis y confidencial, en inglés y español. "
        "Referencias de tratamiento para salud mental y uso de sustancias.",
    ],
    "fr": [
        "Appelez ou envoyez un SMS au 988 — gratuit, confidentiel, 24/7.",
        "Envoyez HOME au 741741 — soutien gratuit par SMS, 24/7.",
        "Appelez le 1-800-950-6264 ou envoyez « HelpLine » au 62640. Lun-ven, 10h-22h (heure de "
        "l'Est). Soutien gratuit par des pairs et orientation — ce n'est pas une ligne de "
        "crise (utilisez le 988 en cas de crise).",
        "Appelez le 1-800-662-HELP (4357), 24/7/365, gratuit et confidentiel, en anglais et "
        "espagnol. Orientation vers des traitements pour la santé mentale et les dépendances.",
    ],
    "hi": [
        "988 पर कॉल या टेक्स्ट करें — मुफ़्त, गोपनीय, 24/7।",
        "741741 पर HOME लिखकर भेजें — मुफ़्त, 24/7 टेक्स्ट सहायता।",
        "1-800-950-6264 पर कॉल करें या 62640 पर \"HelpLine\" लिखकर भेजें। सोम-शुक्र, सुबह 10 से रात "
        "10 बजे (ET)। मुफ़्त पीयर सहायता और रेफ़रल — यह क्राइसिस लाइन नहीं है (संकट के लिए 988 का "
        "उपयोग करें)।",
        "1-800-662-HELP (4357) पर कॉल करें, 24/7/365, मुफ़्त और गोपनीय, अंग्रेज़ी और स्पैनिश में। "
        "मानसिक स्वास्थ्य और नशे से जुड़े उपचार के लिए रेफ़रल।",
    ],
}

# Translated (label, description) for games_data.BREATHING_PATTERNS, keyed the same way.
BREATHING_PATTERNS_I18N = {
    "en": {
        "box": ("Box Breathing", "Equal-count inhale, hold, exhale, and hold — used by athletes and first responders to calm down quickly."),
        "relaxing": ("4-7-8 Relaxing Breath", "A longer exhale than inhale helps activate your body's relaxation response."),
        "belly": ("Deep Belly Breathing", "Slow, deep breaths from the diaphragm to ease tension and lower your heart rate."),
    },
    "es": {
        "box": ("Respiración cuadrada", "Inhala, mantén, exhala y mantén con la misma duración — usada por atletas y socorristas para calmarse rápido."),
        "relaxing": ("Respiración relajante 4-7-8", "Una exhalación más larga que la inhalación ayuda a activar la respuesta de relajación del cuerpo."),
        "belly": ("Respiración abdominal profunda", "Respiraciones lentas y profundas desde el diafragma para aliviar la tensión y bajar el ritmo cardíaco."),
    },
    "fr": {
        "box": ("Respiration carrée", "Inspirez, retenez, expirez et retenez pendant une durée égale — utilisée par les athlètes et les secouristes pour se calmer rapidement."),
        "relaxing": ("Respiration relaxante 4-7-8", "Une expiration plus longue que l'inspiration aide à activer la réponse de relaxation du corps."),
        "belly": ("Respiration abdominale profonde", "Des respirations lentes et profondes depuis le diaphragme pour relâcher la tension et ralentir le rythme cardiaque."),
    },
    "hi": {
        "box": ("बॉक्स ब्रीदिंग", "बराबर गिनती में सांस लें, रोकें, छोड़ें और रोकें — एथलीट और आपातकालीन कर्मी इसका उपयोग जल्दी शांत होने के लिए करते हैं।"),
        "relaxing": ("4-7-8 आरामदायक श्वास", "सांस छोड़ना, सांस लेने से लंबा होने पर शरीर की विश्राम प्रतिक्रिया सक्रिय होने में मदद मिलती है।"),
        "belly": ("गहरी पेट की श्वास", "डायाफ्राम से धीमी, गहरी सांसें तनाव कम करने और हृदय गति घटाने में मदद करती हैं।"),
    },
}

# Translated sense labels for games_data.GROUNDING_STEPS, keyed by sense id.
GROUNDING_LABELS_I18N = {
    "en": {"see": "things you can see", "touch": "things you can touch", "hear": "things you can hear", "smell": "things you can smell", "taste": "thing you can taste"},
    "es": {"see": "cosas que puedes ver", "touch": "cosas que puedes tocar", "hear": "cosas que puedes oír", "smell": "cosas que puedes oler", "taste": "cosa que puedes saborear"},
    "fr": {"see": "choses que vous pouvez voir", "touch": "choses que vous pouvez toucher", "hear": "choses que vous pouvez entendre", "smell": "choses que vous pouvez sentir", "taste": "chose que vous pouvez goûter"},
    "hi": {"see": "चीज़ें जो आप देख सकते हैं", "touch": "चीज़ें जो आप छू सकते हैं", "hear": "चीज़ें जो आप सुन सकते हैं", "smell": "चीज़ें जिन्हें आप सूंघ सकते हैं", "taste": "एक चीज़ जिसे आप चख सकते हैं"},
}

# Translated affirmations, index-aligned with games_data.AFFIRMATIONS.
AFFIRMATIONS_I18N = {
    "es": [
        "Este sentimiento es temporal y pasará.",
        "Estoy haciendo lo mejor que puedo con lo que tengo ahora mismo.",
        "Está bien descansar. Descansar también es productivo.",
        "No tengo que tenerlo todo resuelto hoy.",
        "Tengo derecho a ocupar espacio y pedir ayuda.",
        "Los pequeños pasos también cuentan como progreso.",
        "He superado días difíciles antes, y puedo superar este también.",
        "Mis sentimientos son válidos, incluso cuando son difíciles de explicar.",
        "No soy mis pensamientos. Puedo observarlos sin creer en todos ellos.",
        "Ser amable conmigo mismo no es egoísta, es necesario.",
    ],
    "fr": [
        "Ce sentiment est temporaire, et il va passer.",
        "Je fais de mon mieux avec ce que j'ai en ce moment.",
        "C'est normal de se reposer. Se reposer, c'est aussi productif.",
        "Je n'ai pas besoin de tout comprendre aujourd'hui.",
        "J'ai le droit de prendre de la place et de demander de l'aide.",
        "Les petits pas comptent aussi comme des progrès.",
        "J'ai déjà traversé des jours difficiles, et je peux traverser celui-ci aussi.",
        "Mes émotions sont valables, même quand elles sont difficiles à expliquer.",
        "Je ne suis pas mes pensées. Je peux les observer sans toutes les croire.",
        "Être bienveillant envers moi-même n'est pas égoïste, c'est nécessaire.",
    ],
    "hi": [
        "यह एहसास अस्थायी है, और यह गुज़र जाएगा।",
        "मैं अभी जो कुछ भी है उसके साथ अपना सर्वश्रेष्ठ प्रयास कर रहा/रही हूँ।",
        "आराम करना ठीक है। आराम करना भी उत्पादक है।",
        "मुझे आज ही सब कुछ समझ लेने की ज़रूरत नहीं है।",
        "मुझे जगह लेने और मदद माँगने का अधिकार है।",
        "छोटे कदम भी प्रगति में गिने जाते हैं।",
        "मैंने पहले भी कठिन दिन पार किए हैं, और मैं इसे भी पार कर सकता/सकती हूँ।",
        "मेरी भावनाएँ मान्य हैं, भले ही उन्हें समझाना मुश्किल हो।",
        "मैं अपने विचार नहीं हूँ। मैं उन्हें बिना हर एक पर विश्वास किए देख सकता/सकती हूँ।",
        "खुद के प्रति दयालु होना स्वार्थी नहीं, ज़रूरी है।",
    ],
}


def t(lang: str, key: str, **kwargs) -> str:
    """Look up a translated UI string, falling back to English, then the key itself."""
    value = UI_STRINGS.get(lang, {}).get(key) or UI_STRINGS["en"].get(key) or key
    if kwargs:
        try:
            return value.format(**kwargs)
        except (KeyError, IndexError):
            return value
    return value
