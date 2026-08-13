import webbrowser

MUSIC = {
    "believer": "https://www.youtube.com/watch?v=7wtfhZwyrcc",
    "shape of you": "https://www.youtube.com/watch?v=JGwWNGJdvx8",
    "faded": "https://www.youtube.com/watch?v=60ItHLz5WEA",
}


def play_song(song):
    song = song.lower().strip()

    if song in MUSIC:
        webbrowser.open(MUSIC[song])
        return True

    return False