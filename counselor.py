import streamlit as st
from groq import Groq

st.set_page_config(page_title="CounselAI", page_icon="💬")
st.title("Mental Health Matters")

# Sidebar
with st.sidebar:
    api_key = st.text_input("Enter Groq API Key:", type="password")
    model = st.selectbox(
        "Choose a model:",
        ["llama-3.3-70b-versatile", "llama-3.1-8b-instant"]
    )

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system",
            "content": "You are a professional counselor that helps people with anxiety and stress and suggests daily activities."
        }
    ]

# Display messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if prompt := st.chat_input("How can I help you today?"):
    if not api_key:
        st.error("Please enter your Groq API Key in the sidebar!")
    else:
        client = Groq(api_key=api_key)

        # Add user message
        st.session_state.messages.append({"role": "user", "content": prompt})

        with st.chat_message("user"):
            st.markdown(prompt)

        # Assistant response
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""

            # FIXED: NO comma after create!
            completion = client.chat.completions.create(
                model=model,
                messages=st.session_state.messages,
                stream=True,
            )

for chunk in completion:
    if hasattr(chunk.choices[0].delta, "content"):
        content = chunk.choices[0].delta.content
        if content:
            full_response += content
            message_placeholder.markdown(full_response + "▌")

            message_placeholder.markdown(full_response)

        st.session_state.messages.append(
            {"role": "assistant", "content": full_response}
        )
