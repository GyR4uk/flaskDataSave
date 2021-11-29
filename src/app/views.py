from app import app
from flask import jsonify, request
import json


@app.route("/api", methods=["GET"])
def index():
    message = {
        "apiVersion": "v1.0",
        "status": "200",
    }
    # Making the message looks good
    resp = jsonify(message)
    # Returning the object
    return resp


@app.route("/api/usersAdd", methods=["POST"])
def update_users():
    # Message to the user
    message = {
        "apiVersion": "v1.0",
        "status": "200",
        "message": "Welcome to the Flask API",
    }
    # Making the message looks good
    resp = jsonify(message)
    # Returning the object
    return resp


@app.errorhandler(404)
def page_not_found(e):
    message = {
        "err": {
            "msg": "This route is currently not supported. Please refer API documentation."
        }
    }
    # Making the message looks good
    resp = jsonify(message)
    # Sending OK response
    resp.status_code = 404
    # Returning the object
    return resp
