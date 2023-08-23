#!/usr/bin/python3
from flask import Flask
from models import storage
from api.v1.views import app_views
from flask import Blueprint
import os

"""create an instance of Flask"""
app = Flask(__name__)

"""register a blueprint"""
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown(err):
    """method called when the instance is at the end"""
    storage.close()


if __name__ == "__main__":
    host_hbnb = os.environ.get('HBNB_API_HOST', "0.0.0.0")
    port_hbnb = int(os.environ.get('HBNB_API_PORT', 5000))
    app.run(host=host_hbnb, port=port_hbnb, threaded=True)
