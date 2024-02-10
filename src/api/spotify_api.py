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
        result = get(query_url, headers=header)

        if result.status_code == 200:
            try:
                json_result = result.json()
                return json_result
            except ValueError as e:
                print("Error parsing JSON:", e)
                return None
        else:
            print("Request Failed:", result.status_code)

        return None