#!/usr/bin/python3
""" Write a script that starts a Flask web application """
from flask import Flask
from markupsafe import escape
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """ Hello HBNB! """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ HBNB """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """ C -> followed by Text """
    return f"C {escape(text.replace('_', ' '))}"


if __name__ == '__main__':
    """ Listening on 0.0.0.0, port 5000 """
    app.run(host='0.0.0.0', port=5000)
