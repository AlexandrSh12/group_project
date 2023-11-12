import sqlite3
import tempfile
from pathlib import Path

class DataBase():
    def __init__(self):
        print(tempfile.gettempdir())
        self.__connection = sqlite3.connect(str(Path(tempfile.gettempdir(), "HarryPotter.db")))
        self.__cursor = self.__connection.cursor()

        self.__cursor.execute("CREATE TABLE if not exists scores (id int, score int)")
        self.__connection.commit()
    
    def updateMaxScore(self, score):
        self.__cursor.execute("SELECT score FROM scores WHERE id = 1")
        scores = self.__cursor.fetchall()

        if len(scores) == 0:
            self.__cursor.execute("INSERT INTO scores VALUES (?, ?)", (1, score))
            self.__connection.commit()
            return
        
        maxScore = scores[0][0]
        if score > maxScore:
            self.__cursor.execute("UPDATE scores SET score = (?) WHERE id = 1", (score,))
            self.__connection.commit()
    
    def getMaxScore(self):
        self.__cursor.execute("SELECT score FROM scores WHERE id = 1")
        scores = self.__cursor.fetchall()
        return str(scores[0][0] if len(scores) > 0 else 0)