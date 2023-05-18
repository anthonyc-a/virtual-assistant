# Python Virtual Assistant

This is a Python script that acts as a virtual assistant, utilizing various APIs and libraries to enable speech recognition, text-to-speech conversion, and interaction with the OpenAI GPT-3.5 Turbo model.

## Dependencies

Make sure you have the following dependencies installed:

- `gtts`: This library allows text-to-speech conversion.
- `openai`: The OpenAI Python library for making requests to the GPT-3.5 Turbo model.
- `pygame`: A library for audio playback.
- `speech_recognition`: Provides speech recognition functionality.

You can install the required dependencies using pip:

```shell
pip install gtts openai pygame SpeechRecognition
Setup
```
Before running the script, make sure you have an OpenAI API key. Set your API key by assigning it to the openai.api_key variable at the beginning of the script.

```
openai.api_key = "YOUR_OPENAI_API_KEY"
```
## Usage

To start the virtual assistant, run the script. The assistant will continuously listen for your voice input and respond accordingly. You can communicate with the assistant by speaking and hearing the responses.

### Chat with the Assistant
The assistant uses the OpenAI GPT-3.5 Turbo model for generating responses. It sends the user's message to the model and retrieves the generated response. You can interact with the assistant by speaking and listening to the responses.

To quit the assistant, say "quit". The assistant will respond with "goodbye" and exit.

### Text-to-Speech Conversion
The assistant uses the gtts library for text-to-speech conversion. It converts the assistant's responses to an audio file and plays it using the pygame library. You can control the playback by saying "stop" to pause the audio.

### Speech Recognition
The assistant utilizes the speech_recognition library to recognize your voice input. It listens to your speech using the microphone and converts it to text for processing.

Please note that a working microphone is required for voice input.

## Disclaimer

This virtual assistant is provided as-is with no warranty. Use it at your own risk.
