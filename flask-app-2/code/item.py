import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

# This app works with resources and every resource has to be a class
class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price', # can use request parser to go through input fields
        type=float,
        required=True,
        help="This field cannot be left blank!"
    )

    @jwt_required()
    def get(self, name):
        # find by name may fail prematurely so you might what to add a try except block
        try:
            item = self.find_by_name(name)
        except: # Fails to run the search, raise an exception
            {'message': 'Failed to run the search.'}
        if item:
            return item
        return {'message': 'Item not found'}, 404 # if the find by name fails to find something

    @classmethod
    def find_by_name(cls, name):
        connection = sqlite3.connect('data.db') # connect to the database
        cursor = connection.cursor() # get a cursor

        query = "SELECT * FROM items WHERE name=?" # select the item
        result = cursor.execute(query, (name,)) # run the query
        row = result.fetchone() # fetch a row
        connection.close() # close the connection

        if row: # if the row exist its going to return a json
            return {'item': {'name': row[0], 'price': row[1]}}

    def post(self, name):
        if self.find_by_name(name):   # Error first approach - Handle Errors then do what we want to do
            return {"message": "An item with name '{}' already exists.".format(name)}, 400
            # Something went wrong with the request

        data = Item.parser.parse_args() # parse through the data

        item = {'name' : name, 'price' : data['price']}

        try: # were going to try to insert the item in
            self.insert(item) # there is a chase there may be  problem where the item
            # is not inserted, if this is to happen python has a construct to deal
            # with exceptions. An exception is what python runs whenever an error accurs
        except: # Only runs if there was an error, an exception raised, and if we fail
        # for any reason were just going to return a message
            return {"message": "An error occurred inserting the item."}, 500 # Internal Server Error,
            # that means something went wrong and we can't tell you exactly what, but something went
            # wrong and it is not your fault. - Something didn't go wrong with the request but server
            # messed up, so the user knows they didn't do anything wrong it is just the server that
            # had a problem


        return item, 201

    @classmethod
    def insert(cls, item):
        """
        Insert an item into the database
        """
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "INSERT INTO items VALUES (?, ?)"
        cursor.execute(query, (item['name'], item['price'])) # the cursor may
        # raise an exception if it cannot insert an item into the database

        connection.commit() # the commit may raise an exception of the connection
        # gets closed prematurely
        connection.close()

    @jwt_required()
    def delete(self, name):
        """
        Delete the name in the URL from the database.
        """
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "DELETE FROM items WHERE name=?"
        cursor.execute(query, (name,))

        connection.commit()
        connection.close()

        return {'message': 'Item deleted'}

    def put(self, name):
        """
        Update an item at a given name or insert if not found
        """
        data = Item.parser.parse_args()

        item = self.find_by_name(name)
        updated_item = {'name': name, 'price': data['price']} # this dictionary represents the updated item
        if item is None:
            try:
                self.insert(updated_item)
            except:
                return {"message": "An error occurred inserting the item."}, 500
        else: # update an item if it was already there
            try:
                item.update(updated_item)
            except:
                return {"message": "An error occurred inserting the item."}, 500
        return updated_item

    @classmethod
    def update(cls, item):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "UPDATE items SET price=? WHERE name=?"
        cursor.execute(query, (item['price'], item['name']))

        connection.commit()
        connection.close()


class ItemList(Resource):
    TABLE_NAME = 'items'

    def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM {table}".format(table=self.TABLE_NAME)
        result = cursor.execute(query)
        items = []
        for row in result:
            items.append({'name': row[0], 'price': row[1]})
        connection.close()

        return {'items': items}

# Left off at Retrieving our Item resources from a database 4 min in
