import streamlit as st
import requests
import uuid

# Function to get a response from the LLM
def get_llm_response(session_id, user_ideas):
    api_url = "https://api.chatgpt.com/v1/message"  # Replace with the actual API endpoint
    bearer_token = "your_bearer_token"  # Hard-coded bearer token
    
    # Creating the LLM prompt based on user ideas for a short children’s story
    prompt = f"Maak een kort kinderverhaal over: {user_ideas}"

    # Payload with sessionId and the story prompt
    payload = {
        "sessionId": session_id,
        "chatInput": prompt
    }

    headers = {
        "Authorization": f"Bearer {bearer_token}",
        "Content-Type": "application/json"
    }

    response = requests.post(api_url, json=payload, headers=headers)

    if response.status_code == 200:
        return response.json().get("output", "No response from LLM")
    else:
        return f"Error: {response.status_code}"

# Create a new session ID for the user
session_id = str(uuid.uuid4())

# Set up Streamlit app layout
st.set_page_config(page_title="Kinderverhalen Chat", layout="centered")

# Main header
st.markdown("<h1 style='text-align: center; color: #4A90E2;'>Maak een Kinderverhaal</h1>", unsafe_allow_html=True)

# Subtitle
st.markdown("<p style='text-align: center; color: grey;'>Geef ideeën, en ik maak een kort kinderverhaal voor je!</p>", unsafe_allow_html=True)

# Input form for user ideas
user_ideas = st.text_input("Waar moet het kinderverhaal over gaan?", value="", max_chars=100)

# Display chat history and messages
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Send message button
if st.button("Verstuur"):
    if user_ideas:
        # Display user input (ideas)
        st.session_state["messages"].append(f"**Jij:** {user_ideas}")

        # Get the LLM response (story)
        response = get_llm_response(session_id, user_ideas)

        # Display LLM response (the story)
        st.session_state["messages"].append(f"**Verhaal:** {response}")

# Display chat messages
for message in st.session_state["messages"]:
    st.markdown(f"{message}")

# Footer style
st.markdown(
    "<style>footer {visibility: hidden;} .stTextInput input {background-color: #f1f3f5; border-radius: 8px;}</style>", 
    unsafe_allow_html=True
)