from gtts import gTTS
import openai
import pygame
import speech_recognition as sr

openai.api_key = "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"

pygame.init()

recognizer = sr.Recognizer()
microphone = sr.Microphone()

print("Chat with the Chatbot (say 'quit' to exit)")

def chat_with_gpt3(message):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": message + "in as little information as necessary"}
        ]
    )
    return response.choices[0].message.content


def set_tts(message):
    language = 'en'
    tts = gTTS(message, lang=language, tld='com.au')
    tts.save("output.mp3")

    sound = pygame.mixer.Sound("output.mp3")
    channel = pygame.mixer.Channel(0)  # Use channel 0 for playback

    channel.play(sound)

    pygame.event.set_blocked(None)

    while channel.get_busy():
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            audio = recognizer.listen(source)
        
        try:
            text = recognizer.recognize_google(audio)
            print(text)
            if text.lower() == "stop":
                # Stop the sound when the recognized text is "stop"
                channel.stop()
        except sr.UnknownValueError:
            pass
        except sr.RequestError:
            pass


while True:
    with microphone as source:
        print("Speak now...")
        audio = recognizer.listen(source)

        try:
            user_message = recognizer.recognize_google(audio)
            print("You said:", user_message)

            if user_message.lower() == "quit":
                set_tts("goodbye")
                break

            bot_response = chat_with_gpt3(user_message)
            print("Thinking...")
            print("Chatbot:", bot_response)

            set_tts(bot_response)

        except sr.UnknownValueError:
            set_tts("Please repeat that..")

        except sr.RequestError as e:
            set_tts("Speech recognition request error..")



