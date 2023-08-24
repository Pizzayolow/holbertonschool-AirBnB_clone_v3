#!/usr/bin/python3
"""Route for the State objects"""

from api.v1.views import app_views
from flask import abort, jsonify, request
import json
from models import storage
from models.state import State
from models.city import City


@app_views.route("states/<state_id>/cities", strict_slashes=False)
def states_cities(state_id):
    """return the list of all State objects"""
    list_cities = []
    dict_storage = storage.get(State, state_id)
    if dict_storage is None:
        abort(404)
    cities = dict_storage.cities
    for city in cities:
        dict_city = city.to_dict()
        list_cities.append(dict_city)

    return jsonify(list_cities)


@app_views.route("/cities/<id>", strict_slashes=False)
def city_id(id):
    """return state for the id"""
    obj = storage.get(City, id)
    if obj is None:
        abort(404)
    else:
        return jsonify(obj.to_dict())


@app_views.route("/cities/<id>", methods=["DELETE"], strict_slashes=False)
def delete_city(id):
    """delete a state by id"""
    obj = storage.get(City, id)
    if obj is None:
        abort(404)
    else:
        storage.delete(obj)
        storage.save()
        return jsonify({}), 200


@app_views.route("/states/<id>/cities", methods=["POST"], strict_slashes=False)
def create_city(id):
    """add a state with the name, mandatory"""

    data = request.get_json()
    obj_state = storage.get(State, id)
    if obj_state is None:
        abort(404)
    elif "name" not in data:
        return "Missing name\n", 400
    else:
        obj = City()
        obj.name = data["name"]
        obj_state_id = id
        storage.new(obj)
        storage.save()
        return jsonify(obj.to_dict()), 201


@app_views.route("/cities/<city_id>", methods=["PUT"], strict_slashes=False)
def put_city(city_id):
    """PUT method with the id"""

    obj = storage.get(City, city_id)

    if obj is None:
        abort(404)
    else:
        data = request.get_json()
        if data is None:
            return "Not a JSON\n", 400
        for key, value in data.items():
            if key not in ["id", "created", "updated_at"]:
                setattr(obj, key, value)

        storage.save()
        return jsonify(obj.to_dict()), 200
