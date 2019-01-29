from flask import flask

trial = Flask(__name__)

@app.route("/")
def home():
    return "Hello ladies"

    