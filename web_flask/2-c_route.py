#!/usr/bin/python3
""" Starts a Flask web application """
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_hbnb():
    """ Function that sys Hello Hbnb"""
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """ Function that says hbnb """
    return 'HBNB'


@app.route('/c/<text>')
def c_compliment(text):
    """ Display a message starting with C """
    message = text.replace('_', ' ')
    return 'C %s' % message


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    app.url_map.strict_slashes = False
