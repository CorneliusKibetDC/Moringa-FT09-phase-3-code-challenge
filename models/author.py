

# /models/Author.py
import sqlite3

class Author:
    def __init__(self, name, id=None):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string.")

        self._name = name
        self._id = id

        if id is None:  # Only insert into DB if not loading from DB
            connection = sqlite3.connect('./database/magazine.db')
            cursor = connection.cursor()
            cursor.execute("INSERT INTO authors (name) VALUES (?)", (name,))
            self._id = cursor.lastrowid
            connection.commit()
            connection.close()

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    def articles(self):
        connection = sqlite3.connect('./database/magazine.db')
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM articles WHERE author_id = ?", (self._id,))
        articles = cursor.fetchall()
        connection.close()
        return articles

    def magazines(self):
        connection = sqlite3.connect('./database/magazine.db')
        cursor = connection.cursor()
        cursor.execute("""
            SELECT DISTINCT m.* FROM magazines m
            JOIN articles a ON m.id = a.magazine_id
            WHERE a.author_id = ?
        """, (self._id,))
        magazines = cursor.fetchall()
        connection.close()
        return magazines
