#!/usr/bin/python3
"""routes of index page"""
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status')
def status():
    """return the status of the API"""
    return jsonify(status="OK")


@app_views.route('/stats')
def stats():
    """show the number of class instances"""
    object_stats = {
        'amenities': storage.count('Amenity'),
        'cities': storage.count('City'),
        'places': storage.count('Place'),
        'reviews': storage.count('Review'),
        'states': storage.count('State'),
        'users': storage.count('User')
    }
    return jsonify(object_stats)
