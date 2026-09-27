import streamlit as st
from dotenv import load_dotenv

load_dotenv()

from langchain.chat_models import init_chat_model
from langchain_core.prompts import PromptTemplate


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="CineSage",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

.stApp {
    background:
        linear-gradient(
            rgba(7, 10, 18, 0.90),
            rgba(7, 10, 18, 0.97)
        ),
        url("https://images.unsplash.com/photo-1489599849927-2ee91cede3ba?auto=format&fit=crop&w=2400&q=85");

    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}


/* Main container */

.block-container {
    max-width: 1150px;
    padding-top: 2rem;
    padding-bottom: 4rem;
}


/* ============================================================
   HERO
   ============================================================ */

.hero {
    text-align: center;
    padding: 70px 20px 55px 20px;
}

.hero-title {
    font-size: 5rem;
    line-height: 1;
    font-weight: 800;
    letter-spacing: -3px;
    color: white;
    margin: 0;
    text-shadow: 0 10px 40px rgba(0, 0, 0, 0.5);
}

.hero-accent {
    color: #f4c95d;
}

.hero-subtitle {
    margin-top: 20px;
    font-size: 1.15rem;
    color: #b8becb;
    letter-spacing: 0.2px;
}


/* ============================================================
   GLASS CARDS
   ============================================================ */

.glass-card {
    background: rgba(17, 24, 39, 0.72);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 22px;
    padding: 28px;
    backdrop-filter: blur(18px);
    -webkit-backdrop-filter: blur(18px);
    box-shadow:
        0 20px 60px rgba(0, 0, 0, 0.35);
}


.section-label {
    font-size: 0.75rem;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: #f4c95d;
    margin-bottom: 8px;
}


.section-title {
    color: #ffffff;
    font-size: 1.35rem;
    font-weight: 700;
    margin-bottom: 18px;
}


/* ============================================================
   TEXT AREA
   ============================================================ */

.stTextArea textarea {
    background: rgba(8, 12, 22, 0.85) !important;
    color: #f8fafc !important;

    border: 1px solid rgba(255, 255, 255, 0.10) !important;
    border-radius: 15px !important;

    font-size: 1rem !important;
    line-height: 1.7 !important;

    padding: 18px !important;
}

.stTextArea textarea:focus {
    border: 1px solid #f4c95d !important;
    box-shadow: 0 0 0 1px #f4c95d !important;
}


/* ============================================================
   BUTTON
   ============================================================ */

.stButton > button {
    width: 100%;
    height: 3.2rem;

    border-radius: 14px;
    border: none;

    background: #f4c95d;
    color: #111827;

    font-size: 1rem;
    font-weight: 800;

    transition: all 0.2s ease;
}

.stButton > button:hover {
    background: #ffd978;
    transform: translateY(-2px);

    box-shadow:
        0 10px 30px rgba(244, 201, 93, 0.20);
}


/* ============================================================
   OUTPUT
   ============================================================ */

.output-wrapper {
    margin-top: 30px;
}


.stCodeBlock {
    border-radius: 16px !important;
}


/* ============================================================
   FOOTER
   ============================================================ */

.footer {
    text-align: center;
    margin-top: 55px;
    color: #697386;
    font-size: 0.8rem;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# HERO
# ============================================================

# IMPORTANT:
# No indentation inside this HTML string.
# Otherwise Streamlit may interpret it as a code block.

st.markdown("""
<div class="hero">
<h1 class="hero-title">
Cine<span class="hero-accent">Sage</span>
</h1>

<p class="hero-subtitle">
Turn raw movie descriptions into structured cinematic intelligence.
</p>
</div>
""", unsafe_allow_html=True)


# ============================================================
# MODEL
# ============================================================

model = init_chat_model(
    "openai/gpt-oss-20b",
    model_provider="groq"
)


# ============================================================
# PROMPT TEMPLATE
# ============================================================

prompt = PromptTemplate.from_template("""
You are CineSage, an AI system that processes movie information.

Your task is to analyze the movie description provided below and extract
the most important and useful information from it.

Movie Description:
{movie_text}

Extract the following information:

1. title
   - The name of the movie.

2. year
   - The release year of the movie.
   - If the year is not mentioned, return null.

3. genre
   - Identify the movie's main genres.
   - Return them as a list.

4. director
   - The director of the movie.
   - If the director is not mentioned, return null.

5. main_characters
   - Identify the important characters mentioned in the description.
   - Return them as a list.

6. setting
   - Describe where and when the story takes place.

7. plot
   - Extract the central storyline.
   - Keep it concise and factual.

8. themes
   - Identify the major themes explored in the movie.
   - Return them as a list.

9. summary
   - Generate a clean, easy-to-understand summary of the movie.
   - Keep it between 3 and 5 sentences.
   - Do not include unnecessary details.

Important rules:

- Use ONLY the information provided in the movie description.
- Do not invent or assume information that is not present.
- If information is missing, use null instead of guessing.
- Keep extracted information concise and meaningful.
- Do not include your reasoning or explanation.
- Return ONLY valid JSON.
- Do not use Markdown.
- Do not wrap the JSON inside ```json```.

Return the result using exactly this structure:

{{
    "title": "",
    "year": null,
    "genre": [],
    "director": null,
    "main_characters": [],
    "setting": "",
    "plot": "",
    "themes": [],
    "summary": ""
}}
""")


# ============================================================
# INPUT CARD
# ============================================================

st.markdown("""
<div class="glass-card">
<div class="section-label">CINEMATIC INPUT</div>
<div class="section-title">Movie Description</div>
</div>
""", unsafe_allow_html=True)


movietext = st.text_area(
    "Movie Description",
    placeholder=(
        "Paste the raw movie description here...\n\n"
        "Example: In the near future, Earth is suffering from "
        "severe environmental changes..."
    ),
    height=250,
    label_visibility="collapsed"
)


# ============================================================
# ANALYZE BUTTON
# ============================================================

st.markdown("<div style='height: 12px'></div>", unsafe_allow_html=True)

analyze = st.button(
    "🎬  Analyze Movie"
)


# ============================================================
# PROCESS
# ============================================================

if analyze:

    if not movietext.strip():

        st.warning(
            "Please enter a movie description before analyzing."
        )

    else:

        with st.spinner("CineSage is analyzing the movie..."):

            formatted_prompt = prompt.format(
                movie_text=movietext
            )

            response = model.invoke(formatted_prompt)


        # ====================================================
        # OUTPUT
        # ====================================================

        st.markdown("""
<div class="output-wrapper">

<div class="glass-card">

<div class="section-label">CINESAGE OUTPUT</div>

<div class="section-title">
Structured Movie Information
</div>

</div>

</div>
""", unsafe_allow_html=True)

        st.code(
            response.content,
            language="json"
        )


# ============================================================
# FOOTER
# ============================================================

st.markdown("""
<div class="footer">
CineSage · Movie Intelligence Engine
</div>
""", unsafe_allow_html=True)