import sqlite3
from db import db

# We have told our app we have two models coming from our database - user and item models
class StoreModel(db.Model):
    __tablename__ = 'stores'

    """We have told SQLAlchemy how it can read these items by just looking at the
    columns and when it does look at the columns its going to see the name and
    the price and its going to pump them in straight into the init method and its
    going to be able to create an object for each row in our database. The id
    method will also be passed in but because there is no id parameter in the init
    function it won't be used."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    def __init__(self, name):
        self.name = name

    def json(self):
        return {'name': self.name, 'price': self.price}

    @classmethod
    def find_by_name(cls, name):
        """
        Returns an object of type ItemModel
        """
        #building a query on the database -
        return cls.query.filter_by(name=name).first() # SELECT * FROM items WHERE name=name LIMIT 1

    def insert(self):
        """
        Insert an item into the database
        """
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "INSERT INTO items VALUES (?, ?)"
        cursor.execute(query, (self.name, self.price)) # the cursor may
        # raise an exception if it cannot insert an item into the database

        connection.commit() # the commit may raise an exception of the connection
        # gets closed prematurely
        connection.close()

    def update(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "UPDATE items SET price=? WHERE name=?"
        cursor.execute(query, (self.price, self.name))

        connection.commit()
        connection.close()
