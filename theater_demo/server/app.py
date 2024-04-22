#!/usr/bin/env python3

# 1a. Set Up Imports
from flask import Flask, make_response, request

# use export FLASK_APP=app.py, export FLASK_RUN_PORT=5555, flask run
# include app.run at bottom of file and run file with python file.py (see bottom of page)
app = Flask(__name__)

# 2. Create a / route that returns Hello World
# 2a. Run the server with `flask run --debug` to check if its in the browser
@app.route('/')
def index():
    return 'Hello world'


# by default, flask returns JSON
# return {} returns a dictionary, not an object instance
# ~~~~make_response(prod) to return an instance of an object~~~
# jsonify(prod) to return an instance of an object
# res = Response() create a response object
@app.route('/longest-movies')
def get_longest_movies():
    prod = {
        "title": "dune 2",
        "genre": "sci-fi",
        "length": 230
    }
    #not returning an object, just an dictionary
    return prod

# string - refers to data type
# title - refers to name of our parameter

@app.route('/productions/<int:title>')
def production_integer(title):
    prod = {
        "title": title,
        "genre": "integer",
        "length": 90
    }

    return make_response(prod)

@app.route('/productions/<string:title>')
def production_string(title):
    prod = {
        "title": title,
        "genre": "string",
        "length": 90
    }

    return make_response(prod)

# 5. View the path and host with request context
# 5a. Import 'request'
# 5b. Create route `context` 
# 5c. use ipdb
@app.route('/my-context')
def my_context():
    my_context = {
        "path": request.path,
        "host": request.host
    }
    return make_response(my_context)

# 6. Use the before_request request hook, what this hook does is up to you. You could hit a breakpoint, print something to server console or anything else you can think of.
@app.before_request 
def runs_before():
    print("running before", request.path)
    #play around with current context of request
    #import ipdb; ipdb.set_trace()

# don't forget to pass in response and return it
@app.after_request
def runs_after(response):
    print("running after")
    #play around with current context of response
    #in postman - you will see loading while on the ipdb breakpoint
    #type continue to go past breakpoint and finish request
    #import ipdb; ipdb.set_trace()
    return response



# Note: If you'd like to run the application as a script instead of using `flask run`, uncomment the line below 
# and run `python app.py`

if __name__ == '__main__':
    app.run(port=5555, debug=True)