from flask import Flask, request, render_template
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required

from security import authenticate, identity

app = Flask(__name__) # Flask is going to be our app and this app is going to have routes

app.secret_key = 'jose'
# imported from Flask-restful allows us to very easily add these routes it (okay for this resource you can get and post)
api = Api(app)

jwt = JWT(app, authenticate, identity) #/auth

# In memory database
items = []

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
        item = next(filter(lambda x: x['name'] == name, items), None)
        for item in items:
            if item['name'] == name:
                return item
        return {'item': item}, 200 if item else 404

    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items), None) is not None:   # Error first approach - Handle Errors then do what we want to do
            return {"message": "An item with name '{}' already exists.".format(name)}, 400

        data = Item.parser.parse_args()

        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201

    def delete(self, name):
        global items
        items = list(filter(lambda x: x['name'] != name, items))
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
    def get(self):
        return {'items': items}

api.add_resource(Item, '/item/<string:name>') # now this resource we have creating now can be accessiable via our API route
api.add_resource(ItemList, '/items')

app.run(port=5000, debug=True)
