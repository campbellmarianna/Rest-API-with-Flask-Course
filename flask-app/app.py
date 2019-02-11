# your browser handles request
# a flask application receives a request from your browser
    # a request may ask for the homepage
# a server must be created to understand that request
# classes always start with a captle is a class, start with lowercase is a package
from flask import Flask

app = Flask(__name__) # create a object in Flask and give it a unique name - give each file a unique name

@app.route('/') # http://www.google.com/ # the route or the endpoint it is going to understand - the end slash means that it is the home page of the application
def home(): # create a method home
    return "Hello, world!" # return a response to our browser so that it receives something back and can show something on our website

app.run(port=5000)# we have to tell the app to start running
# we have to tell the a specific port an area of the computer where your app is going to receiving your request and returning your response through


# What we know
    # Going to a site does a GET request
    # This normally returns HTML
    # We can return other things
    # We can do other than GET EX: POST
# What is a REST API?
# It's a way of thinking about how a web server responds to your requests
# It doesn't respond with just data
# It responds with resources (the server ask for something and responses with data this is different the server is asking for a resource a thing in the server)
# Resources?
# Similar to object-oriented programming
# Think of the server as having resources, and each is able to interact with the pertinent request

# Stateless
# Another key feature is that REST is supposed to be stateless
# This means one request connot depend on any other requests
# The server only knows about the current request, and not any previous requests

# For example:
# POST item/chair creates an item
# The server does not know the item now exists
# GET /item/chair then goes to the database and checks to see if the item is there or an error otherwise
# To get an item you do not need to have created an item before--the item could be in the database previously

#Another example
# A user logs in to a web application
# The webserver does not know the user is logged in (since it does not remember any state)
# What do we do?
# The web application must send enough data to identify the user in every request, or else the server won't associate the request with the user

# Confusing?
# It's always confusing initially
# As we program these APIs, a lot of these things will come naturally because often they make sense
# Ask questions at any time, I'm always availble to help
