import json
from api.spotify_api import SpotifyAPI
from data_processing.spotify_parser import SpotifyParser
import pandas as pd

## https://open.spotify.com/playlist/5GUWrtpZ83SjfHTh50Wnu8?si=30d97af8262e4551
def main():
    url = input("Input spotify playlist url: ")
    spotify_instance = SpotifyAPI()
    response = spotify_instance.get_playlist(url)
    result = SpotifyParser().spotifyPlaylistMapper(response)
    return

if __name__ == "__main__":
    main()