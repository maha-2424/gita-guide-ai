import streamlit as st

def show_banner():

    st.markdown("""
    <div style="
        background: linear-gradient(90deg,#FF9933,#FFD700);
        padding:25px;
        border-radius:15px;
        text-align:center;
        color:black;
        margin-bottom:20px;
    ">

    <h1>🕉️ GitaGuide AI</h1>

    <h3>Your Personal Bhagavad Gita Mentor</h3>

    <p>
    Ancient Wisdom • Modern AI • Daily Guidance
    </p>

    </div>
    """, unsafe_allow_html=True)