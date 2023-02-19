# from app import db
# from app.models.User import User
from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token


auth = Blueprint("auth", __name__, url_prefix="/")
profile = Blueprint("profile", __name__, url_prefix="/profile")


# auth route to return JWT access tokens
@auth.route("/token", methods=["POST"])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    if username != "test" or password != "test":
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)