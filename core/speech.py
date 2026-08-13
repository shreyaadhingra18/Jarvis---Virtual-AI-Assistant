import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()


def speak(text):
    print("JARVIS:", text)
    engine.say(text)
    engine.runAndWait()


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
        print("YOU SAID:", text)
        return text

    except sr.UnknownValueError:
        print("I couldn't understand that.")
        return ""

    except sr.RequestError as e:
        print("Speech recognition error:", e)
        return ""