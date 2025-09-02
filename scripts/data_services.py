from spotify_connect import SpotifyConnection
from sql_services import SQLConnection
import time

class DataServices:
    def __init__(self):
        spotify_handler = SpotifyConnection()
        self.spotify_connection = spotify_handler.get_instance()
        self.sql_connection = SQLConnection()

    def chart_data_processing(self, chart_elems):
        for date, state in chart_elems.items():
            for city, tracks in state.items():
                for song, artists in tracks.items():
                    self.sql_connection.insertChart(date, city, song, artists) # this is raw href data
        
                    
# results.append(self.spotify_connection.track(song))
