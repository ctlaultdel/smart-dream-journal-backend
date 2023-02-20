from app import db
from app.models.User import User
from flask import Blueprint, jsonify, request, abort, make_response
from flask_jwt_extended import create_access_token

# Authorization blueprint ~ public routes
auth_bp = Blueprint("auth", __name__, url_prefix="/")


# route to request JWT access token
@auth_bp.route("/token", methods=["POST"])
def login():
    request_body = request.get_json()
    username = request.json.get("username", None)
    email = request.json.get("email", None)
    password = request.json.get("password", None)
    # check for username/email with password
    if not (username and password) and not (email & password):
        abort(make_response({"message": "username or email required for login"}, 400))
    # fetch user matching username/email and password
    user = User.query.filter_by(**request_body).first()
    # handle incorrect credentials
    if not user:
        abort(make_response({"message": "Credentials are incorrect"}, 401))
    # create access token for user
    access_token = create_access_token(identity=user.id)
    return jsonify(access_token=access_token)

# route to register new account
@auth_bp.route("/register", methods=["POST"])
def register():
    request_body = request.get_json()
    try:
        username = request_body["username"]
        email = request_body["email"]
        password = request_body["password"]
    except KeyError as e:
        abort(make_response({"message": f"Request body must include {e}"}, 400))
    new_user = User(username=username, email=email, password=password)
    new_user.save()
    return make_response({"message": f"{username} successfully created"}, 201)