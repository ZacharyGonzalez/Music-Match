import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd
import requests

load_dotenv()

CLIENT_SECRET=os.getenv("SPOTIFY_TOKEN")
CLIENT_ID=os.getenv("CLIENT_ID")
REDIRECT_URI="http://127.0.0.1:8080"

url = "https://spotifycharts.com/regional/global/daily/latest/download"
r=requests.get(url,allow_redirects=True)
r.raise_for_status()
df = pd.read_csv(r.text)
print(df.head())

def main():
    pass

if __name__ == "__main__":
    main()

"""
scope = "user-library-read"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope=scope))

results = sp.search(q="track:doxy", type="track", limit=10)
for track in results:
    print(track['name'], "-", track['artists'][0]['name'])



results = sp.current_user_saved_tracks()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])

"""