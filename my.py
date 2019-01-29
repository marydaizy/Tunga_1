from flask import flask

trial = Flask(__name__)

@trial.route("/")
def home():
    return "Hello py_ladies"

    