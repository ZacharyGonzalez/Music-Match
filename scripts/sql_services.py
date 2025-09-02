from sql_connect import SQLConnection

class SQL_services():
    def __init__(self):
        self.sql_services = SQLConnection()

    def connect_check(self):    
        self.sql_services.check_connected()

    def close_connection(self):
        self.sql_services.close()

    def insert_chart_data(self, week, city, songname, artists): # make a data package for this
        self.sql_services.insertChart(week, city, songname, artists)