from core.speech import speak, listen
from core.commands import process_command
from tools.news import get_news


def main():

    speak("Initializing Jarvis.")

    while True:

        text = listen()

        if not text:
            continue

        if "jarvis" not in text.lower():
            continue

        speak("Yes.")

        command = listen()

        if command:
            process_command(command)


if __name__ == "__main__":
    main()