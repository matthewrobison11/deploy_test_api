# Import the Flask object from the flask package
from flask import Flask, request, jsonify

# -----------------------------------------------------
#
# "Initialize"/"Instantiate" your flask app
# A good default name is `app`; some tools will
# look for that name by default
#
# Adam talks some about "dunders" and __name__
app = Flask(__name__)


# -----------------------------------------------------
#
# requests.get("website.com/")
@app.route("/")
def index():
    return "Welcome! the endpoints for data are atom and multiply"


# Create our first endpoint
# requests.get("website.com/atom")
@app.route("/atom")
def atom():
    return "hydrogen has 1 electron"


@app.route("/<name>")
def greet(name):
    return f"hello {name}"


# -----------------------------------------------------
#
# Add the code that will run your app!
#
# Use `debug=True` while developing
# (auto refresh and debugging features)
#
# Adam talks more about "dunders" and the common
# __name__ == "__main__"
#
# As we add more stuff, add it above this
# our app.run() will be the bottom of our file
# if __name__ == "__main__":
#     app.run(debug=True)

# -----------------------------------------------------
#
# Actually run your app!
#
# I'll use the command line to run this whole file at once
# Open terminal -> `cd` as needed -> `python flask-hola-mundo.py`
#
# Then use your web browser to view the results!
# Which kind of HTTP request/verb did our browser use to load the text?


# -----------------------------------------------------
#
# Add an endpoint with parameters
#
# Maybe a multiply endpoint that multiplies params x and y
# You'll need to import request from flask
#
# Use your endpoint via browser to multiply different numbers
#
# Break it how a user would
#
# Add default values for the parameters


@app.route("/multiply")
def multiply():
    x = request.args.get("x", type=int)
    y = request.args.get("y", type=int)

    product = x * y

    data = {"x": x, "y": y, "product": product}
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)


# -----------------------------------------------------
#
# Update the multiply output to return JSON with more info
#
# The JSON can show what was x, what was y, and finally the answer
# You'll need to import jsonify from flask
#
# Use your endpoint via browser
#
# Use your endpoint via python + requests
# Break it and see how it looks from this perspective


# -----------------------------------------------------
#
# Add a "dynamic" route (oooohhh)
#
# idk, we can do something like saying hi to a name... ? not creative rn


# -----------------------------------------------------
#
# If we get this far class is over... work on bonus assignments or leave ig
# bye
