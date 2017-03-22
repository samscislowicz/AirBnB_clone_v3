#!/usr/bin/python3
"""
module
"""
from api.v1.views import app_views
from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
from models import storage
import os


app = Flask(__name__)
CORS(app)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown(self):
    """
    closing function
    """
    storage.close()


@app.errorhandler(404)
def page_not_found(error):
    """
    404 error page
    """
    not_found = {'error': 'Not found'}
    return jsonify(not_found)


if __name__ == "__main__":
    host_ip = os.getenv('HBNB_API_HOST', '0.0.0.0')
    host_port = os.getenv('HBNB_API_PORT', '5000')
    app.run(host=host_ip, port=host_port)
