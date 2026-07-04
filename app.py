from banner import show_banner
from daily_verse import get_daily_verse
import streamlit as st

from chatbot import ask_gita_ai
from mood_agent import detect_mood
from verse_agent import get_verse
from action_agent import get_action
from reflection_agent import get_reflection

st.set_page_config(
    page_title="🕉️ GitaGuide AI",
    page_icon="🕉️",
    layout="wide"
)

# ---------- Sidebar ----------

with st.sidebar:

    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/Om_symbol.svg/512px-Om_symbol.svg.png",
        width=120
    )

    st.title("🕉️ GitaGuide AI")

    st.markdown("---")

    st.write("### 🌸 Daily Wisdom")

    st.info(
        "Focus on your actions, not on the results.\n\n"
        "— Bhagavad Gita 2.47"
    )

    st.markdown("---")

    st.markdown("---")

st.write("### ⚙️ Technologies")

st.write("✅ Python")

st.write("✅ Streamlit")

st.write("✅ Gemini AI")

st.write("✅ Multi-Agent Design")

st.write("✅ Bhagavad Gita Knowledge Base")

st.markdown("---")

st.success("Version 1.0")

# ---------- Main Page ----------

show_banner()
daily = get_daily_verse()

st.markdown("## 🌸 Verse of the Day")

st.info(
    f"📖 {daily['verse']}\n\n{daily['text']}"
)

st.markdown("---")

question = st.text_area(
    "💬 What's on your mind today?",
    height=120
)

if st.button("Ask GitaGuide AI"):

    if question.strip():

        mood = detect_mood(question)

        verse = get_verse(mood)

        action = get_action(mood)

        reflection = get_reflection(mood)

        with st.spinner("Thinking..."):
            answer = ask_gita_ai(question, verse)

        st.divider()

        icons = {
    "Career": "💼",
    "Education": "📚",
    "Stress": "🧘",
    "Relationship": "❤️",
    "General": "🌸"
}

        st.success(f"{icons.get(mood, '🌸')} Detected Mood: {mood}")

        st.info(
            f"📖 {verse['verse']}\n\n{verse['text']}"
        )

        st.markdown("## 🤖 AI Guidance")
        st.write(answer)

        st.markdown("## 🎯 Today's Action")
        st.success(action)

        st.markdown("## 💭 Reflection")
        st.warning(reflection)
        
st.markdown("---")

st.caption(
    "🕉️ GitaGuide AI | Built with Python, Streamlit, Gemini AI and Bhagavad Gita Knowledge Base"
)