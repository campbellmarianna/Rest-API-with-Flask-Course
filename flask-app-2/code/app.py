from flask import Flask
from flask_restful import Resource, Api # Resource - something our API represents (if our api is concerned with students then our api will return student)

app = Flask(__name__) # Flask is going to be our app and this app is going to have routes

# imported from Flask-restful allows us to very easily add these routes it (okay for this resource you can get and post)
api = Api(app)

# This app works with resources and every resource has to be a class
class Student(Resource): # this is going to be a copy with a couple of things changed
    def get(self, name):
        return {'student': name}

api.add_resource(Student, '/student/<string:name>') #http://127.0.0.1;5000/student/Rolf # now this resource we have creating now can be accessiable via our API route

app.run(port=5000)
