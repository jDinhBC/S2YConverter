import json
from dotenv import load_dotenv
import os
import base64
from requests import post
import re

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

def get_token():
    auth_string = client_id + ":" + client_secret
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

def get_auth_header(token):
    return {"Authorization": "Bearer "+ token}

def get_user_id(url):
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



token = get_token()