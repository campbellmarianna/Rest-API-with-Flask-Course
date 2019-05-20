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
        item = self.find_by_name(name)
        if item:
            return item
        return {'message': 'Item not found'}, 404

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

        data = Item.parser.parse_args() # parse through the data

        item = {'name': name, 'price': data['price']}

        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "INSERT INTO items VALUES (?, ?)"
        cursor.execute(query, (item['name'], item['price']))

        connection.commit()
        connection.close()

        return item, 201

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
        data = Item.parser.parse_args()

        item = next(filter(lambda x: x['name'] == name, items), None)
        if item is None:
            item = {'name': name, 'price': data['price']}
            items.append(item)
        else:
            item.update(data)
        return item

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
