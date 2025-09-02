import mysql.connector
import os
from dotenv import load_dotenv

class SQL_Handler():
    load_dotenv()

    def __init__(self):

        self.db = mysql.connector.connect(
            host = os.getenv("HOST"),
            user = os.getenv("USER"),
            password = os.getenv("PASSWORD"),
            database = os.getenv("DATABASE")
        )
        self.cursor = self.db.cursor()

    def check_connected(self):
        self.cursor.execute("SELECT DATABASE()")
        result = self.cursor.fetchone()
        if result:
            print(f"CONNECTED TO DATABASE: {result[0]}")
        else:
            print("Failed to connect to SQL Database.")

    def close(self):
        self.cursor.close()
        self.db.close()

    def insertSong(self,city, songname, artists, spotifyURI):
        values = f"'{city}', '{songname}','{artists}', '{spotifyURI}', "
        query = f"INSERT INTO employees (id, name, ) VALUES ({values})" # note the f-string expression
        self.cursor.execute(query)
        self.db.commit()