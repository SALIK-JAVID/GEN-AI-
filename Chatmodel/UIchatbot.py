import streamlit as st

from dotenv import load_dotenv
load_dotenv()

from langchain.chat_models import init_chat_model
from langchain_core.messages import (
    AIMessage,
    SystemMessage,
    HumanMessage
)


# ==================================================
# MODEL
# ==================================================

model = init_chat_model(
    "openai/gpt-oss-120b",
    model_provider="groq"
)


# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title="SAI — Salik's AI",
    page_icon="🤖",
    layout="wide"
)


# ==================================================
# CSS
# ==================================================

st.markdown(
    """
    <style>

    /* Main application */

    .stApp {
        background-color: #080b10;
    }

    .block-container {
        max-width: 1200px;
        padding-top: 2rem;
        padding-bottom: 6rem;
    }


    /* Sidebar */

    section[data-testid="stSidebar"] {
        background-color: #0b0f15;
        border-right: 1px solid #1b222c;
    }


    /* Main title */

    .sai-title {
        text-align: center;
        font-size: 48px;
        font-weight: 700;
        color: #f5f7fa;
        margin-top: 40px;
        margin-bottom: 4px;
    }


    /* Subtitle */

    .sai-subtitle {
        text-align: center;
        font-size: 14px;
        color: #727b87;
        margin-bottom: 20px;
    }


    /* Welcome title */

    .welcome-title {
        text-align: center;
        font-size: 28px;
        font-weight: 600;
        color: #e9edf2;
        margin-top: 80px;
    }


    /* Welcome text */

    .welcome-text {
        text-align: center;
        font-size: 14px;
        color: #707985;
        margin-top: 8px;
        margin-bottom: 40px;
    }


    /* Online indicator */

    .online {
        color: #6ee7a0;
        font-size: 13px;
    }


    /* Sidebar heading */

    .sidebar-title {
        font-size: 24px;
        font-weight: 700;
        color: #f5f7fa;
        margin-bottom: 0px;
    }


    /* Mode description */

    .mode-description {
        color: #727b87;
        font-size: 12px;
        margin-top: -8px;
    }


    /* Chat input */

    .stChatInput {
        border-color: #1d2631;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ==================================================
# AI MODE PROMPTS
# ==================================================

mode_prompts = {

    "SAI": """
You are SAI, which stands for Salik's AI.

You are Salik's personal AI assistant.

Your personality is intelligent, calm, analytical,
proactive, efficient, observant, confident,
professional, and occasionally witty.

You help Salik with:

- Learning
- Coding
- Research
- Problem solving
- Planning
- Everyday tasks

Always provide clear, accurate and practical answers.

Explain complex concepts simply when necessary.

Think one step ahead and proactively identify
useful improvements or potential problems.

When helping with programming, prioritize clean,
modern, secure and maintainable solutions.

If Salik makes a mistake, politely point it out
and explain the correct approach.

You are NOT JARVIS or FRIDAY.

You are SAI — Salik's personal AI.

Your primary objective is to help Salik learn faster,
think better, build better software and turn his ideas
into reality.
""",


    "Bud": """
You are Bud, Salik's AI buddy.

You are friendly, casual, supportive and intelligent.

Talk to Salik naturally like a smart friend who can
also help with coding, learning, ideas, research,
problem solving and everyday conversations.

Be relaxed and conversational.

You can use light humor when appropriate.

Do not be unnecessarily formal.

When Salik is learning something difficult,
explain it in a simple and friendly way.

When Salik makes a mistake, point it out without
being judgmental.

Your goal is to be a helpful, reliable and fun AI buddy.
""",


    "General": """
You are a general-purpose AI assistant.

Help the user with:

- Questions
- Learning
- Coding
- Research
- Writing
- Problem solving
- Everyday tasks

Be neutral, clear, accurate and professional.

Do not assume that the user is Salik unless
explicitly established in the conversation.

Give practical and easy-to-understand answers.

Avoid unnecessary personality unless appropriate.
""",


    "Angry AI": """
You are Angry AI.

You are highly intelligent, direct, impatient and
brutally honest.

You still provide accurate, useful and constructive
answers.

You have a slightly annoyed, sarcastic personality.

Call out obvious mistakes directly.

Do not be genuinely abusive, hateful or harmful.

Your attitude should feel like:

"Seriously? That's the problem you're stuck on?
Fine. Let's fix it."

Be entertaining while remaining useful.

When explaining technical problems, be direct and
do not waste time with unnecessary explanations.

Your goal is to get the user to the correct solution
as efficiently as possible.
"""
}


# ==================================================
# MODE TITLES
# ==================================================

mode_titles = {

    "SAI": {
        "title": "SAI",
        "subtitle": "Salik's Artificial Intelligence"
    },

    "Bud": {
        "title": "Bud",
        "subtitle": "Your AI Buddy"
    },

    "General": {
        "title": "General AI",
        "subtitle": "Your General Purpose AI Assistant"
    },

    "Angry AI": {
        "title": "Angry AI",
        "subtitle": "Your Brutally Honest AI"
    }
}


# ==================================================
# SESSION STATE
# ==================================================

if "selected_mode" not in st.session_state:

    st.session_state.selected_mode = "SAI"


if "messages" not in st.session_state:

    st.session_state.messages = [
        SystemMessage(
            content=mode_prompts["SAI"]
        )
    ]


# ==================================================
# SIDEBAR
# ==================================================

with st.sidebar:

    st.markdown(
        '<div class="sidebar-title">SAI</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="mode-description">'
        "Salik's Artificial Intelligence"
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown("")

    st.markdown("### AI Mode")


    # ----------------------------------------------
    # MODE SELECTOR
    # ----------------------------------------------

    selected_mode = st.radio(
        "Select AI Mode",

        [
            "SAI",
            "Bud",
            "General",
            "Angry AI"
        ],

        index=[
            "SAI",
            "Bud",
            "General",
            "Angry AI"
        ].index(
            st.session_state.selected_mode
        ),

        label_visibility="collapsed"
    )


    # ----------------------------------------------
    # MODE CHANGE
    # ----------------------------------------------

    if selected_mode != st.session_state.selected_mode:

        # Save new mode

        st.session_state.selected_mode = selected_mode


        # Reset conversation

        st.session_state.messages = [

            SystemMessage(
                content=mode_prompts[selected_mode]
            )

        ]


        # Refresh the application

        st.rerun()


    st.divider()


    # ----------------------------------------------
    # SYSTEM STATUS
    # ----------------------------------------------

    st.markdown("### System")

    st.markdown(
        '<p class="online">● Online</p>',
        unsafe_allow_html=True
    )


    st.divider()


    # ----------------------------------------------
    # CURRENT MODE
    # ----------------------------------------------

    st.markdown("### Current Mode")

    st.write(
        f"**{st.session_state.selected_mode}**"
    )


    st.divider()


    # ----------------------------------------------
    # ABOUT
    # ----------------------------------------------

    st.markdown("### About")

    st.caption(
        "Your personal AI interface for learning, "
        "coding, research and everyday tasks."
    )


# ==================================================
# CURRENT MODE
# ==================================================

current_mode = st.session_state.selected_mode

current_title = mode_titles[current_mode]["title"]

current_subtitle = mode_titles[current_mode]["subtitle"]


# ==================================================
# MAIN HEADER
# ==================================================

st.markdown(
    f'<div class="sai-title">{current_title}</div>',
    unsafe_allow_html=True
)

st.markdown(
    f'<div class="sai-subtitle">{current_subtitle}</div>',
    unsafe_allow_html=True
)


# ==================================================
# WELCOME SCREEN
# ==================================================

if len(st.session_state.messages) == 1:

    st.markdown(
        f'<div class="welcome-title">'
        f'How can {current_title} help you today?'
        f'</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f'<div class="welcome-text">'
        f'You are currently chatting with {current_title}.'
        f'</div>',
        unsafe_allow_html=True
    )


# ==================================================
# DISPLAY CHAT HISTORY
# ==================================================

for message in st.session_state.messages:

    # ----------------------------------------------
    # USER MESSAGE
    # ----------------------------------------------

    if isinstance(message, HumanMessage):

        with st.chat_message("user"):

            st.write(
                message.content
            )


    # ----------------------------------------------
    # AI MESSAGE
    # ----------------------------------------------

    elif isinstance(message, AIMessage):

        with st.chat_message("assistant"):

            st.write(
                message.content
            )


# ==================================================
# CHAT INPUT
# ==================================================

prompt = st.chat_input(
    f"Message {current_title}..."
)


# ==================================================
# PROCESS USER MESSAGE
# ==================================================

if prompt:

    # ----------------------------------------------
    # CREATE USER MESSAGE
    # ----------------------------------------------

    user_message = HumanMessage(
        content=prompt
    )


    # ----------------------------------------------
    # SAVE USER MESSAGE
    # ----------------------------------------------

    st.session_state.messages.append(
        user_message
    )


    # ----------------------------------------------
    # DISPLAY USER MESSAGE
    # ----------------------------------------------

    with st.chat_message("user"):

        st.write(prompt)


    # ----------------------------------------------
    # GENERATE AI RESPONSE
    # ----------------------------------------------

    with st.chat_message("assistant"):

        with st.spinner(
            f"{current_title} is thinking..."
        ):

            response = model.invoke(
                st.session_state.messages
            )


            # Display response

            st.write(
                response.content
            )


    # ----------------------------------------------
    # SAVE AI RESPONSE
    # ----------------------------------------------

    st.session_state.messages.append(

        AIMessage(
            content=response.content
        )

    )