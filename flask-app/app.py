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

# HTTP is one of the most popular protocal to create interations and allowing interactions between to internet connected elements
# What is a web server?
    # hardware
    # software designed to accept incoming web requests
    # For example, Google has many web servers
    # When we go to http://www.google.com in our browser, we send something to a web server
        # Then it can decide to respond
        # Left off at 38. HTTP Verbs 01:52
# What do we send?
    # WHen you go to http://www.google.com, you send the following:
        # GET / HTTP/1.1
        # Host: www.google.com
        # What does this mean:
            # It is a GET request
                # The server then sees GET (a verb - tells the server to some extent what the server will return, it is what we expect of the server) / (path - what we want out of the server) HTTP (protocol - the most popular protocal)/1.1
# So, what?
    # That's it!
    # The server sees that, and then there's code
    # The code may interpret the GET request in many different ways
# For example ...
    # It may give you an error, if / is not found
    # It may give you an error, if HTTP is not supported
    # It may give you an error, if the server is unavailable
    # It may give you HTML code back (which is what it normally does)
    # It may give you some text back
    # It may give you nothing back
# What else?
    # Going to any page in your browser will do the same
# Differences
# THe only difference is what the server on the other end responds with
    # Twitter responds with the Twitter HTML
    # git-scm responds with the git-scm HTML
    # Google responds witht the Google HTML
# What else?
    # Going to a page will always do a GET # the browser (Chrome, Safari) is configured to do a GET request
    # But there are many other things we can do, such as POST, DELETE, PUT, OPTIONS, HEAD and much more
    # Each server responds differently to each, but they normally have the same meaning in each
# HTTP Verbs
    # GET Retrieve something EX: GET /item/1
    # POST Receive data, and use it EX: POST/item # with a post request normally, you have to send some data along the post request
    # PUT Make sure something is there EX: PUT/item # check if there if something is there it will update it
    # DELETE Remove somehting EX: DELETE /item/1
