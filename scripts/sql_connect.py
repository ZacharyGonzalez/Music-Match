import mysql.connector
import os
from dotenv import load_dotenv

class SQLConnection():
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

    def insertChart(self, week, city, songname, artists):
        values = f"'{week}', {city}', '{songname}','{artists}'"
        query = f"INSERT INTO employees (week, city, songname, artists) VALUES ({values})" # note the f-string expression
        self.cursor.execute(query)
        self.db.commit()