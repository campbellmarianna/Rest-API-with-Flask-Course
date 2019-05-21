import sqlite3
from db import db

class UserModel(db.Model): # entend models to db model
    __tablename__ = 'users'

    id = db.Column(db.Integar, primary_key=True) # primary key makes it is easy to search based on id
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self, _id, username, password):
        # these properties must match the columns for them to be saved to the database
        self.id = _id
        self.username = username
        self.password = password
        self.something = 'hi' # we can have other properties but it won't be
        # saved to the database. It also won't give us an error, it will exist
        # in the object, but it won't be in anyway related to the database, it
        # won't be stored it won't be read from the database

    @classmethod
    def find_by_username(cls, username):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE username=?"
        result = cursor.execute(query, (username,))
        row = result.fetchone()
        if row:
            user = cls(*row) # positional argument
        else:
            user = None

        connection.close()
        return user

    @classmethod
    def find_by_id(cls, _id):
        print("CAME HERE")
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE id=?"
        result = cursor.execute(query, (_id,))
        row = result.fetchone()
        if row:
            user = cls(*row) # positional argument
        else:
            user = None

        connection.close()
        return user
