from app import db
from app.models.User import User
from flask import Blueprint, jsonify, request, abort, make_response
from flask_jwt_extended import get_jwt_identity, jwt_required

profile = Blueprint("profile", __name__, url_prefix="/profile")

# profile home page route ~ protected
@jwt_required()
@profile.route("", methods=["GET"])
def display_profile_home_page():
    # username = get_jwt_identity()
    return make_response({"username": "Hello World!"}, 200)