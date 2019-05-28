import sqlite3
from db import db

# We have told our app we have two models coming from our database - user and item models
# We create a model instead a resource because our resource uses the
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

    items = db.relationship('ItemModel', lazy='dynamic') # lists of item models - one to many

    def __init__(self, name):
        self.name = name
    # util we call this json method we are not going into the table to get the methods - this is slower
    def json(self):
        return {'name': self.name, 'items': [item.json() for item in self.items.all()]}

    @classmethod
    def find_by_name(cls, name):
        """
        Returns an object of type ItemModel
        """
        #building a query on the database -
        return cls.query.filter_by(name=name).first() # SELECT * FROM items WHERE name=name LIMIT 1


    def save_to_db(self):
        """
        Insert an item into the database
        """
        db.session.add(self) # add to the session
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
