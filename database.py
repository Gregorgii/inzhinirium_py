import sqlite3


class Database:
    def __init__(self):
        self.conn = sqlite3.connect("scores.db")
        self.cursor = self.conn.cursor()

    def create_table(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS scores (name TEXT, score INTEGER)")

    def insert_score(self, name, score):
        self.cursor.execute("INSERT INTO scores VALUES (?, ?)", (name, score))
        self.conn.commit()

    def get_top_scores(self):
        self.cursor.execute("SELECT name, score FROM scores ORDER BY score DESC LIMIT 5")
        top_scores = self.cursor.fetchall()
        return top_scores
