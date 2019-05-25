from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel

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
        """
        Returns the item itself
        """
        # find by name may fail prematurely so you might what to add a try except block
        try:
            item = ItemModel.find_by_name(name)
        except: # Fails to run the search, raise an exception
            {'message': 'Failed to run the search.'}
        if item:
            return item.json()
        return {'message': 'Item not found'}, 404 # if the find by name fails to find something

    def post(self, name):
        if ItemModel.find_by_name(name):   # Error first approach - Handle Errors then do what we want to do
            return {"message": "An item with name '{}' already exists.".format(name)}, 400
            # Something went wrong with the request

        data = Item.parser.parse_args() # parse through the data

        item = ItemModel(name, data['price'])

        try: # were going to try to insert the item in
            item.insert() # there is a chase there may be  problem where the item
            # is not inserted, if this is to happen python has a construct to deal
            # with exceptions. An exception is what python runs whenever an error accurs
        except: # Only runs if there was an error, an exception raised, and if we fail
        # for any reason were just going to return a message
            return {"message": "An error occurred inserting the item."}, 500 # Internal Server Error,
            # that means something went wrong and we can't tell you exactly what, but something went
            # wrong and it is not your fault. - Something didn't go wrong with the request but server
            # messed up, so the user knows they didn't do anything wrong it is just the server that
            # had a problem
        return item.json(), 201

    @jwt_required()
    def delete(self, name):
        """
        Delete the name in the URL from the database.
        """
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "DELETE FROM items WHERE name=?"
        cursor.execute(query, (name,))

        connection.commit() # save what we've done
        connection.close()

        return {'message': 'Item deleted'}

    def put(self, name):
        """
        Update an item at a given name or insert if not found
        """
        data = Item.parser.parse_args()

        item = ItemModel.find_by_name(name) # Item is the item we found in the database
        updated_item = ItemModel(name, data['price']) # A new item - same name but different price
        if item is None:
            try:
                updated_item.insert()
            except:
                return {"message": "An error occurred inserting the item."}, 500
        else: # update an item if it was already there
            try:
                updated_item.update()
            except:
                return {"message": "An error occurred inserting the item."}, 500
        return updated_item.json()


class ItemList(Resource):
    def get(self):
        # Were getting all the items and looping through them - using list comprehension
        return { 'items': [item.json() for item in ItemModel.query.ll] }
        # Another implementation mapping a function to an element - using map
        # (helpful when working with others programming in a diffrent language,
        # also more stackable )
        # return { 'items': list(map(lambda x: x.json(), ItemModel.query.all()))}
