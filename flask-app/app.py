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
