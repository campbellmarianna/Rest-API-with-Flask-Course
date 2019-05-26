from db import db
# The model is an API, it exposes to endpoints to methods, find_by are to interfaces as far reading and retrieving from the database
class UserModel(db.Model): # entend models to db model
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True) # primary key makes it is easy to search based on id
    # id auto increments, database manager SQLAlchemy gives the object an id, if we didn't want an an auto increment id we can create our own
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self, username, password):
        # these properties must match the columns for them to be saved to the database
        self.username = username
        self.password = password
        self.something = 'hi' # we can have other properties but it won't be
        # saved to the database. It also won't give us an error, it will exist
        # in the object, but it won't be in anyway related to the database, it
        # won't be stored it won't be read from the database

    def save_to_db(self):
        db.session.add(self) # put delete if you wanted to remove something
        db.session.commit()

    @classmethod
    #The server doesn't care if the API is built - uses the API to communicate with the user and the database
    #the same layout of programming are the same everywhere you look
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first() # SELECT * FROM USERS - the query builder is an object by
        # which can build queries

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
