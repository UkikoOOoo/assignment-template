# assignment-template
SD5913 - Assignment template

# 😙 Talking to AI directly with our mouths!!

A Streamlit chatbot powered by Ollama that allows users to talk to an AI assistant directly with their mouths, without the need for text input.

## How to use
- Press the `Please speak...` and say something.
- Press the `End of speech.` to end the saying.
- You can press `play button` to listen what AI talk about.

## Features

- Speech-to-text conversion using `streamlit_mic_recorder`.
- AI chat responses powered by OpenAI's chat completions API.
- Text-to-speech playback using `gTTS` libraries.

## Setup

Before you start, ensure you have the following prerequisites installed:

1. Python 3.8 or later.
2. Streamlit. 
```bash
python -m streamlit run audio_chatbot.py 
```
3. To ensure your `microphone permissions` are allowed.
4. Open the `LM studio-developer` and running the server status.
5. Ensure the  `Server Port` and the name of `Loaded model` is same in the code with LM studio.
```bash
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

 response = client.chat.completions.create(
            model = "Meta-Llama-3.1-8B-Instruct-GGUF",
            messages = st.session_state.messages,
            stream = True,
        )
```
6. `streamlit_mic_recorder` library for speech recognition.
7. `torch` library for text-to-speech.
8. `gTTS` library for text-to-speech.

You can install the required libraries using pip:

```bash
pip install -r requirements.txt
```
