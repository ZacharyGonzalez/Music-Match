from spotify_connect import SpotifyConnection
import json
import time
# NO more reading require, just pass the data from the collector to the SQL connection.
sp = SpotifyConnection()
connection = sp.get_instance()
with open('./docs/test.txt','r') as o, open('./docs/trial.txt','w') as p:
    elems = json.load(o)
    results = []
    for date,city in elems.items():
        for city, track in city.items():
            for song, artists in track.items():
                spotify_uri=song
                results.append(connection.track(spotify_uri))
                json.dump(results,p,indent=2)
                time.sleep(4)
                
