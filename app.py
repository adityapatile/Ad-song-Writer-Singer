import streamlit as st
import openai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Configure OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_ad(theme):
    """Generate an advertisement based on the theme."""
    try:
        response = openai.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a creative advertising copywriter."},
                {"role": "user", "content": f"Create a compelling advertisement for the theme: {theme}. Include a catchy headline, main copy, and a call to action."}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error generating ad: {str(e)}"

def generate_song(theme):
    """Generate song lyrics based on the theme."""
    try:
        response = openai.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a creative songwriter."},
                {"role": "user", "content": f"Write a song about the theme: {theme}. Include verses, chorus, and a bridge. Make it catchy and memorable."}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error generating song: {str(e)}"

# Streamlit UI
st.title("🎵 Ad & Song Generator")
st.write("Generate creative advertisements and songs based on your theme!")

# Theme input
theme = st.text_input("Enter your theme:", placeholder="e.g., Summer Vacation, New Technology, etc.")

if theme:
    # Create two columns for the results
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📢 Advertisement")
        if st.button("Generate Ad"):
            with st.spinner("Generating advertisement..."):
                ad = generate_ad(theme)
                st.write(ad)
    
    with col2:
        st.subheader("🎼 Song")
        if st.button("Generate Song"):
            with st.spinner("Generating song..."):
                song = generate_song(theme)
                st.write(song)

# Add some styling
st.markdown("""
<style>
    .stButton>button {
        width: 100%;
    }
</style>
""", unsafe_allow_html=True) 