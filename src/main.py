from spotify_api import SpotifyAPI
from spotify_parser import SpotifyParser
import pandas as pd

def main():
    url = input("Input spotify playlist url: ")
    spotify_instance = SpotifyAPI()
    response = spotify_instance.get_playlist(url)

    return

if __name__ == "__main__":
    main()