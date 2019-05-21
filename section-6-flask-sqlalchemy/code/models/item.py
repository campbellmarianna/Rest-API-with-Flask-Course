import sqlite3
from db import db

# We have told our app we have two models coming from our database - user and item models
class ItemModel(db.Model):
    __tablename__ = 'items'

    """We have told SQLAlchemy how it can read these items by just looking at the
    columns and when it does look at the columns its going to see the name and
    the price and its going to pump them in straight into the init method and its
    going to be able to create an object for each row in our database. The id
    method will also be passed in but because there is no id parameter in the init
    function it won't be used."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price db.Column(db.Float(precision=2)) # floating point number a decimal number

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def json(self):
        return {'name': self.name, 'price': self.price}

    @classmethod
    def find_by_name(cls, name):
        """
        Returns an object of type ItemModel
        """
        connection = sqlite3.connect('data.db') # connect to the database
        cursor = connection.cursor() # get a cursor after creating the connection to execute SQL statements

        query = "SELECT * FROM items WHERE name=?" # select the item
        result = cursor.execute(query, (name,)) # run the query
        row = result.fetchone() # fetch a row
        connection.close() # close the connection

        if row: # if the row exist its going to return a json
            return cls(*row) # passes each element in the row into the class init method

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
