from flask import Flask

trial = Flask(__name__)

@trial.route("/")
def home():
    return "Hello py_ladies"

    