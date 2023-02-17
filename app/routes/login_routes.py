import uuid
from app import db
from app.models.User import User
from flask import Blueprint, jsonify, abort, make_response, request
from app.models.validation_checkers import validate_model

auth = Blueprint("auth", __name__, url_prefix="/")

# authentification routes
@auth.route("", methods=["POST"])
def login():
    request_body = request.get_json()
    user = User.query.filter_by(username=request_body["username"])[0]
    if user and request_body["password"]==user.password:
        token = uuid.uuid4()
        return {"token": token}
    else:
        abort(make_response({
            "message": "username or password incorrect"
        }, 404))

@auth.route("/signup")
def signup():
    return "Signup"

@auth.route("/logout")
def logout():
    return "Logout"




# @main_bp.route("", methods=["GET"])
# def display_homepage():
#     return "Main page"


# profile_bp = Blueprint("profile", __name__, url_prefix="/profile")

# @profile_bp.route("")
# def my_profile():
#     response_body = {
#         "username": "Lollapalarza",
#         "about": "My profile"
#     }
#     return response_body


# # login route
# login_bp = Blueprint("login", __name__, url_prefix="/login")
# @login_bp.route("", methods=["GET", "POST"])
# def display_login():
#     form = LoginForm()
#     return form

# # register route
# register_bp = Blueprint("register", __name__, url_prefix="/register")
# @register_bp.route("", methods=["GET", "POST"])
# def register_user():
#     form = RegisterForm()
#     return form
# callback route

# logout route