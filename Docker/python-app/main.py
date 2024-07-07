from flask import Flask
from os import environ

app = Flask(__name__)

@app.route('/')
def index():
    return '<p>Hello world!</p>'

port = environ.get('PORT', 5500)
host = environ.get('HOST', '0.0.0.0')
app.run(host, port)