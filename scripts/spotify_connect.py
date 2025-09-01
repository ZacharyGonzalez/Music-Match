
import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

class SpotifyConnection:
    load_dotenv()    

    def __init__(self):
        scope = "user-library-read"
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id = os.getenv("CLIENT_ID"),
            client_secret = os.getenv("CLIENT_SECRET"),
            redirect_uri = os.getenv("REDIRECT_URI"),
            scope=scope))
        
    def get_instance(self):
        return self.sp
        

