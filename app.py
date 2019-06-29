from flask import Flask

app = Flask(__name__)

@app.route('/<name>')
def index(name):
    return "<h1>Welcome to the first flask app" + name + "</h1>"
