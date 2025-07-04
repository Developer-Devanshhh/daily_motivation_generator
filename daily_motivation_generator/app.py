import streamlit as st
from gemini_api import generate_motivation

# Streamlit App UI
st.set_page_config(page_title="Daily Motivation Generator", page_icon="✨")

st.title("🌟 Daily Motivation Generator")
st.markdown("Feeling down, distracted, or just need a boost? Select your current mood and receive motivation ✨")

# List of mood/situation options
moods = [
    "anxious",
    "tired",
    "burnt out",
    "stressed",
    "unmotivated",
    "lost",
    "need focus",
    "need hope",
    "confused",
    "want encouragement"
]

selected_mood = st.selectbox("How are you feeling right now?", moods)

if st.button("Generate Motivation ✨"):
    with st.spinner("Talking to the universe..."):
        message = generate_motivation(selected_mood)
        st.success("Here’s your message:")
        st.markdown(f"**🧘 {message}**")
