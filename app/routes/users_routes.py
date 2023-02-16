from flask import Blueprint, jsonify, request, make_response, abort
from app import db
from app.models.User import User
from app.models.Entry import Entry
from app.models.validation_checkers import validate_model

# initialize entries blueprint
users_bp = Blueprint("user", __name__, url_prefix="/users")

# get all users route
@users_bp.route("", methods=["GET"])
def display_all_users():
    users = User.query.all()
    response_users = []
    for user in users:
        response_users.append(user.to_dict())
    return jsonify(response_users)

# create user route
@users_bp.route("", methods=["POST"])
def create_user():
    request_body = request.get_json()
    attribute_requirements = ["username", "password"]
    for req in attribute_requirements:
        if req not in request_body:
            abort(make_response({
                "message" : f"Failed to create a planet because {req} missing"
                }, 400))
    new_user = User.from_dict(request_body)
    db.session.add(new_user)
    db.session.commit()
    return make_response({"message":"user has been created successfully"}, 201)