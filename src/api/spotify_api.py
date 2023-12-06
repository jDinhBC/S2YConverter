import json
from dotenv import load_dotenv
import os
import base64
from requests import post, get
import re

class SpotifyAPI:

    def __init__(self):
        load_dotenv()
        self.client_id = os.getenv("CLIENT_ID")
        self.client_secret = os.getenv("CLIENT_SECRET")
        self.token = self.get_token()
        self.base_url = 'https://api.spotify.com/v1/'

    def get_token(self):
        auth_string = self.client_id + ":" + self.client_secret
        auth_bytes = auth_string.encode("utf-8")
        auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

        url = "https://accounts.spotify.com/api/token"
        headers = {
            "Authorization": "Basic " + auth_base64,
            "Content-Type": "application/x-www-form-urlencoded"
        }
        data = {"grant_type": "client_credentials"}
        result = post(url, headers=headers, data=data)
        json_result = json.loads(result.content)
        token = None
        if ("access_token" not in json_result):
            token = "Unable to retrieve access token"
        token = json_result["access_token"]
        return token

    def get_auth_header(self):
        return {"Authorization": "Bearer "+ self.token}

    def get_user_id(self, url):
        # takes url of spotify user profile and extracts id
        url = input("Enter spotify profile url: ")
        pattern = r'https://open\.spotify\.com/user/([A-Za-z0-9]+)'
        checkUrl = re.fullmatch(pattern, url)

        if not checkUrl:
            return "Url does not fit the criteria"
        
        matches = re.search(pattern, url)

        if not matches:
            return "User ID not found"
        
        user_id = matches.group(1)
        return user_id

    def get_playlist_id(self, url):
        # Takes url and extracts playlist ID
        pattern = r"https://open\.spotify\.com/playlist/([^/?]+)"
        match = re.match(pattern, url)
        if match:
            return match.group(1)
        else:
            return "Url does not fit the Spotify playlist url criteria"
        
    def get_playlist(self, url):
        header = self.get_auth_header()
        query = f"playlists/{self.get_playlist_id(url)}"
        query_url = self.base_url + query
        print(query_url)
        result = get(query_url, headers=header)
        return result