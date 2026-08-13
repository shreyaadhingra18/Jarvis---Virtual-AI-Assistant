import os
from gtts import gTTS
import pygame
import speech_recognition as sr

recognizer = sr.Recognizer()


def speak(text):
    print("JARVIS:", text)

    tts = gTTS(text=text, lang="en")
    tts.save("output.mp3")

    pygame.mixer.init()
    pygame.mixer.music.load("output.mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.mixer.music.unload()
    os.remove("output.mp3")


def listen():
    with sr.Microphone() as source:
        print("Listening...")

        audio = recognizer.listen(
            source,
            timeout=10,
            phrase_time_limit=5
        )

    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio)

        print("YOU SAID:", repr(text))
        return text

    except sr.UnknownValueError:
        print("I couldn't understand that.")
        return None

    except sr.RequestError as e:
        print("Google recognition error:", e)
        return None