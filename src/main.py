from spotify_api import SpotifyAPI
import pandas as pd

def main():
    url = input("Input spotify playlist url: ")
    spotify_instance = SpotifyAPI()
    result = spotify_instance.get_playlist(url)
    return

if __name__ == "__main__":
    main()