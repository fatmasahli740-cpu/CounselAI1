import streamlit as st
from groq import Groq

st.set_page_config(page_title="Groq Chatbot", page_icon="💬")
st.title("Groq-Powered Assistant")

# Sidebar for API Key and Model Selection
with st.sidebar:
    #api_key = st.secrets["GROQ_API_KEY"]
    api_key = st.text_input("Enter Groq API Key:", type="password")
    model = st.selectbox("Choose a model:", ["llama-3.3-70b-versatile", "llama-3.1-8b-instant"])

# Initialize Chat History
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": "You are a professional counselor that communicates with people suffering anxiety and stress and help them overcome their problems and fears and give them daily activities."}]

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User Input
if prompt := st.chat_input("How can I help you today?"):
    if not api_key:
        st.error("Please enter your Groq API Key in the sidebar!")
    else:
        client = Groq(api_key=api_key),
        
        # Add user message to history
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Generate Assistant Response
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""
            
            # Request streaming completion
# Request streaming completion
            completion = client.chat.completions.create(
                model=model,
                messages=st.session_state.messages,
                stream=True,
            ) # <--- This closing parenthesis is mandatory

# The "for" loop to catch the AI's words as they arrive
for chunk in completion:
                if chunk.choices[0].delta.content:
                    content = chunk.choices[0].delta.content
                    full_response += content
                    message_placeholder.markdown(full_response + "▌")

                    message_placeholder.markdown(full_response)
                    
                    # Save assistant response to history
                    st.session_state.messages.append({"role": "assistant", "content": full_response})
