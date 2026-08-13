from core.speech import speak
from tools import browser
from tools.news import get_news
from tools.music import play_song


def process_command(command):

    command = command.lower()

    if "open google" in command:
        speak("Opening Google")
        browser.open_google()

    elif "open youtube" in command:
        speak("Opening YouTube")
        browser.open_youtube()

    elif "open github" in command:
        speak("Opening GitHub")
        browser.open_github()

    elif "open instagram" in command:
        speak("Opening Instagram")
        browser.open_instagram()

    elif "open gmail" in command:
        speak("Opening Gmail")
        browser.open_gmail()

    elif "open linkedin" in command:
        speak("Opening LinkedIn")
        browser.open_linkedin()

    elif "open qm plus" in command:
        speak("Opening QMPlus")
        browser.open_qmplus()

    elif "news" in command:
        speak("Fetching the latest news.")

        headlines = get_news()

        if not headlines:
            speak("Sorry, I couldn't get the news.")
            return

        for headline in headlines[:5]:
            speak(headline)
    elif command.startswith("play "):
        song = command[5:].strip()

        if play_song(song):
            speak(f"Playing {song}")
        else:
            speak("Sorry, I don't have that song.")

    else:
        return False

    return True