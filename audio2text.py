import streamlit as st
from streamlit_mic_recorder import speech_to_text

st.title("🐝Talking to AI directly with our mouths!!")
# original
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

# show message
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# audio input
text = speech_to_text(language='en', start_prompt="Please speak...", stop_prompt="End of speech.")
if text:
    #st.write("Transcribed Text:", text)
    # audio2text into message
    st.session_state.messages.append({"role": "user", "content": text})
    st.chat_message("user").write(text)

# mennual text input
#prompt = st.text_input("You:", key="user_input")
#if prompt:
    #st.session_state.messages.append({"role": "user", "content": prompt})
    #st.chat_message("user").write(prompt)