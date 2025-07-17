# app.py
import streamlit as st
from model import get_groq_reply
import time

st.set_page_config(page_title="ayan bot", layout="centered")
st.title("🤖 Chat with ayan")

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": "You are a helpful assistant."}]

for msg in st.session_state.messages:
    if msg["role"] != "system":
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

user_input = st.chat_input("Ask me anything...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Prepare streaming UI block
    with st.chat_message("assistant"):
        response_stream = get_groq_reply(st.session_state.messages)
        full_response = ""
        response_placeholder = st.empty()

        for chunk in response_stream:
            full_response += chunk
            response_placeholder.markdown(full_response + "▌")  # show typing cursor
            time.sleep(0.1)
        response_placeholder.markdown(full_response)  # remove cursor after done

    st.session_state.messages.append({"role": "assistant", "content": full_response})
