import streamlit as st
from groq import Groq

st.set_page_config(page_title="CounselAI", page_icon="💬")
st.title("Mental Health Matters")

# Sidebar for API Key and Model Selection
with st.sidebar:
    # Use the local variable 'api_key' instead of forcing st.secrets
    api_key = st.text_input("Enter Groq API Key:", type="password")
    model = st.selectbox("Choose a model:", ["llama-3.3-70b-versatile", "llama-3.1-8b-instant"])

# Initialize Chat History
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": "You are a therapist that communicates with people suffering anxiety and stress and help them overcome their problems and fears and heal them and give them daily activities."}]

# Display previous messages (excluding system prompt)
for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# User Input
if prompt := st.chat_input("How can I help you today?"):
    if not api_key:
        st.error("Please enter your Groq API Key in the sidebar!")
    else:
        # Initialize client using the 'api_key' variable from the text_input
        client = Groq(api_key=api_key)
        
        # Add user message to history
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Generate Assistant Response
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""
            
            # Request streaming completion
            # CORRECTED: Initialize the client using the sidebar variable
        client = Groq(api_key=api_key)
        
        # Add user message to history
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Generate Assistant Response
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""
            
# Ensure client is defined right before the call
        client = Groq(api_key=api_key)
        completion = client.chat.completions.create(
            model=model,
            messages=st.session_state.messages,
            stream=True,
        )

        for chunk in completion:
                # Check if content exists to avoid 'None' errors
                if chunk.choices[0].delta.content:
                    content = chunk.choices[0].delta.content
                    full_response += content
                    message_placeholder.markdown(full_response + "▌")
            
              message_placeholder.markdown(full_response)
        
        # Save assistant response to history
        st.session_state.messages.append({"role": "assistant", "content": full_response})
