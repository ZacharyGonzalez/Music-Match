import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd
import json
load_dotenv()

CLIENT_SECRET=os.getenv("CLIENT_SECRET")
CLIENT_ID=os.getenv("CLIENT_ID")
REDIRECT_URI="http://127.0.0.1:8080"
print(CLIENT_SECRET)
print(CLIENT_ID)

scope = "user-library-read"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope=scope))

df = pd.read_csv('regional-us-weekly-2025-08-28.csv')
spotify_uri=df['uri'][0]
print(df)
results = sp.track(spotify_uri)
print(json.dumps(results,indent=2))

def main():
    pass

if __name__ == "__main__":
    main()





"""
results = sp.current_user_saved_tracks()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])

"""