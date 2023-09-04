
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello, world!'


@app.route('/about')
def about():
    return 'This is the last assignment of Back-end'
