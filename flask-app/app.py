from flask import Flask, jsonify, request, render_template

app = Flask(__name__) # create a object in Flask and give it a unique name - give each file a unique name


# JSON - is a list of dictionaries - very useful to send data between applications - JSON is not a dictionary - JSON is text as a string
# JSON always uses double quotes
stores = [{
        'name': 'My Wonderful Store',
        'items': [{'name': 'My Item', 'price': 15.99}]
}]

@app.route('/')
def home():
    return render_template('index.html')


# We are a server
# POST - used to receive data
# GET - used to send data back only

# POST /store data: {name:}
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)


# GET /store/<string:name>
@app.route('/store/<string:name>') # 'http://127.0.01:5000/store/some_name'
def get_store(name):
    for store in stores: # Iterate over stores
        if store['name'] == name: # if the store name matches, return it
            return jsonify(store)
    return jsonify({'message': 'Store not found.'}) # if none match, return an error message

# GET /store
@app.route('/store')
def get_stores():
    return jsonify({'stores': stores}) # our dictionary has a key stores and a value our stores # we make are stores a dictionary so we can jsonify that


# POST /store/<string:name>/item {name:, price:}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name' : request_data['name'],
                'price' : request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message': 'Store not found.'}) # if store is not found this error will run


# GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})
    return  jsonify({'message' :'Store not found.'})


app.run(port=5000)# we have to tell the app to start running
# we have to tell the a specific port an area of the computer where your app is going to receiving your request and returning your response through

# The Header is the first thing that gets analyzed by the server.
    # The first thing that Flask is going to look at is header to see what this request is

# Postman is extremely useful for testing APIs in development

# A REST API is going to be an interface between your program and other programs that call your API.
