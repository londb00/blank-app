import streamlit as st
import requests
import openai
import uuid

# Set up OpenAI API (replace with your OpenAI API key)
openai.api_key = "your-openai-api-key"

# Function to generate a short children's story
def generate_story(keywords):
    # Creating the prompt for the story based on user-provided keywords
    prompt = f"Maak een kort kinderverhaaltje over: {keywords}"

    try:
        # Call OpenAI API
        response = openai.Completion.create(
            engine="text-davinci-003",  # You can change the engine if needed
            prompt=prompt,
            max_tokens=150,
            temperature=0.7
        )
        
        # Extracting the story from the response
        story = response.choices[0].text.strip()
        return story

    except Exception as e:
        return f"Er is iets misgegaan: {str(e)}"

# Streamlit app layout
st.set_page_config(page_title="Kinderverhalen Generator", layout="centered")

# Main title and description
st.markdown("<h1 style='text-align: center; color: #4A90E2;'>Kinderverhaal Generator</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: grey;'>Voer een paar steekwoorden in, en ik maak een kort kinderverhaal voor je!</p>", unsafe_allow_html=True)

# Input for user keywords
user_keywords = st.text_input("Waar moet het kinderverhaal over gaan?", value="", max_chars=100)

# Generate button
if st.button("Maak Verhaaltje"):
    if user_keywords:
        # Display loading message
        with st.spinner("Verhaaltje wordt gemaakt..."):
            # Generate the story
            story = generate_story(user_keywords)

            # Display the story
            st.markdown(f"### Verhaal:\n{story}")
    else:
        st.error("Voer een paar steekwoorden in om te beginnen.")

# Footer style
st.markdown(
    "<style>footer {visibility: hidden;} .stTextInput input {background-color: #f1f3f5; border-radius: 8px;}</style>", 
    unsafe_allow_html=True
)