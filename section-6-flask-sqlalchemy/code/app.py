from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

app = Flask(__name__) # Flask is going to be our app and this app is going to have routes
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db' # were saying data.db is going to run at the root of our folder
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # the reason why we say this
# essentially in order to know when an object had changed but not being saved to the
# database the extension flask_sqlalchemy was tracking every change that we made
# to the SQLAlchemy session and that took some resources, now were turning it off
# because SQLAlchemy itself, the main library has its own modification tracker
# which is a bit better, so this turns off the Flask SQLAlchemy Modification
# tracker it does not turn off the SQLAlchemy Modification Tracker. This is only
# changing the extensions behaviors not the underlining SQLAlchemy behavior.
app.secret_key = 'jose'
# imported from Flask-restful allows us to very easily add these routes it (okay for this resource you can get and post)
api = Api(app)

# important to import what you want to be in the database such as Item and Store models if you want them as tables in the database
# SQLAlchemy creates the data.db for us but it doesn't put any tables in it, sp were going to tell to do so
@app.before_first_request # before the first request runs it will do the code below
def create_tables():
    db.create_all()

jwt = JWT(app, authenticate, identity) #/auth

api.add_resource(Item, '/item/<string:name>') # now this resource we have creating now can be accessiable via our API route
api.add_resource(ItemList, '/items')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    """We are importing this here because of a thing called circular imports, our
    item models and things are going to import db as well so if we import db at
    the top and we're also going to import the models at the  when we import the
    model, the model is going to import the db and the db is going to be importted
    here in the app that is going to create a circular import"""
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
