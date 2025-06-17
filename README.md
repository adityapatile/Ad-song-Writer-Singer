# Ad & Song Generator

A Streamlit application that generates creative advertisements and songs based on a given theme using OpenAI's GPT-4 model.

## Features

- Generate creative advertisements with headlines, main copy, and calls to action
- Create original songs with verses, chorus, and bridge
- Clean and intuitive user interface
- Real-time generation using OpenAI's GPT-4 model

## Setup

1. Clone this repository
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the root directory and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

## Usage

1. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```
2. Open your web browser and navigate to the provided local URL (usually http://localhost:8501)
3. Enter a theme in the text input field
4. Click the "Generate Ad" or "Generate Song" buttons to create content

## Requirements

- Python 3.7+
- OpenAI API key
- Internet connection

## Note

Make sure to keep your OpenAI API key secure and never share it publicly. 