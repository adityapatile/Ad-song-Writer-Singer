import streamlit as st
import openai
from dotenv import load_dotenv
import os
import base64
from io import BytesIO
import requests

# Load environment variables
load_dotenv()

# Initialize session state for API key
if 'openai_api_key' not in st.session_state:
    st.session_state.openai_api_key = None

# Sidebar for API key input
with st.sidebar:
    st.title("🔑 API Configuration")
    api_key = st.text_input("Enter your OpenAI API Key:", type="password")
    if api_key:
        st.session_state.openai_api_key = api_key
        st.success("✅ API Key saved!")

# Main app
st.title("🎵 Song Generator")
st.write("Generate creative songs based on your theme!")

# Check if API key is set
if not st.session_state.openai_api_key:
    st.warning("⚠️ Please enter your OpenAI API key in the sidebar to continue.")
    st.stop()

# Configure OpenAI client
client = openai.OpenAI(api_key=st.session_state.openai_api_key)

def generate_song(theme):
    """Generate song lyrics based on the theme."""
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a creative songwriter. Write short, catchy songs with a maximum of 100 words. Format them with clear sections labeled as [Verse 1], [Chorus], and [Verse 2]."},
                {"role": "user", "content": f"Write a short, catchy song about the theme: {theme}. Keep it under 100 words total. Include two short verses and one chorus. Make it memorable and easy to sing."}
            ],
            temperature=0.7,
            max_tokens=300  # Adjusted max tokens for 100-word output
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error generating song: {str(e)}"

def generate_voice_audio(text):
    """Generate audio using OpenAI's text-to-speech API."""
    try:
        st.write("Debug: Starting voice generation...")
        
        # Split text into smaller chunks if it's too long
        max_chars = 1000
        text_chunks = [text[i:i+max_chars] for i in range(0, len(text), max_chars)]
        
        all_audio = bytearray()
        
        for chunk in text_chunks:
            response = client.audio.speech.create(
                model="tts-1",
                voice="alloy",  # You can choose from: alloy, echo, fable, onyx, nova, shimmer
                input=chunk
            )
            
            st.write(f"Debug: Processing chunk of {len(chunk)} characters...")
            
            # Convert the response to bytes
            audio_bytes = response.content
            
            if audio_bytes:
                st.write("Debug: Successfully received audio chunk")
                all_audio.extend(audio_bytes)
            else:
                st.error("Failed to generate audio chunk")
                return None
        
        if all_audio:
            st.write("Debug: Successfully generated complete audio")
            return bytes(all_audio)
        else:
            st.error("No audio was generated")
            return None
            
    except Exception as e:
        st.error(f"Error generating audio: {str(e)}")
        st.write("Debug: Full error details:", e)
        return None

# Theme input
theme = st.text_input("Enter your theme:", placeholder="e.g., Summer Vacation, New Technology, etc.")

if theme:
    # Create container for the song
    song_container = st.container()
    
    # Generate song button
    if st.button("Generate Song"):
        with st.spinner("Generating song..."):
            try:
                song = generate_song(theme)
                if song and not song.startswith("Error"):
                    # Store the song in session state
                    st.session_state['current_song'] = song
                    song_container.write(song)
                else:
                    st.write(song)
                    st.error("Failed to generate song. Please try again with a different theme.")
            except Exception as e:
                st.error(f"An unexpected error occurred: {str(e)}")

# Voice generation section
if 'current_song' in st.session_state:
    st.subheader("🎤 Voice Generation")
    if st.button("Generate Voice Version"):
        with st.spinner("Generating voice audio..."):
            audio_data = generate_voice_audio(st.session_state['current_song'])
            if audio_data:
                st.audio(audio_data, format="audio/mpeg")
                # Store audio data in session state
                st.session_state['current_audio'] = audio_data
            else:
                st.error("Failed to generate audio. Please try again.")

# Add some styling
st.markdown("""
<style>
    .stButton>button {
        width: 100%;
    }
</style>
""", unsafe_allow_html=True) 