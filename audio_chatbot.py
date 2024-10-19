import streamlit as st
from streamlit_mic_recorder import speech_to_text
from openai import OpenAI
from gtts import gTTS
import io

st.title("😙Talking to AI directly with our mouths!!")
st.caption("🚀 A Streamlit chatbot powered by Ollama")

# Point to the local server
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}] 
    
if "msg" not in st.session_state:
    st.session_state["msg"] = ""

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

placeholder = st.empty()

with placeholder.container():
    prompt = speech_to_text(language='en', start_prompt="Please speak...", stop_prompt="End of speech.")

    if prompt:

        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)

        response = client.chat.completions.create(
            model = "Meta-Llama-3.1-8B-Instruct-GGUF",
            messages = st.session_state.messages,
            stream = True,
        )

        msg = ""

        def stream_response():
            global msg
            for chunk in response:
              print(chunk)
              part = chunk.choices[0].delta.content
              if part:
                  msg += part
                  yield part

        st.chat_message("assistant").write_stream(stream_response)
        st.session_state.messages.append({"role": "assistant", "content": st.session_state["msg"]})

        # Use gTTS to generate speech
        tts = gTTS(msg, lang='en', slow = False)

        # Use BytesIO to create a streamable object
        mp3_buffer = io.BytesIO()
        tts.write_to_fp(mp3_buffer)
       
        mp3_buffer.seek(0)  

        # Play the audio using Streamlit's audio component
        st.audio(mp3_buffer, format='audio/mpeg')