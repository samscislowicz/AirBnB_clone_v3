#!/usr/bin/python3
"""

"""
from flask import jsonify
from api.v1.views import app_views
from models import storage


@app_views.route("/status")
def status():
    ok = {"status": "OK"}
    return jsonify(ok)


@app_views.route("/stats/")
def stats():
    list_models = {"amenities": "Amenity", "cities": "City", "places": "Place",
                "reviews": "Review", "states": "State", "users": "User"}
    dic = {}
    for cls in list_models.keys():
        dic[list_models[cls]] = storage.count(cls)
    return jsonify(list_dict)
