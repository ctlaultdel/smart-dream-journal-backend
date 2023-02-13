from flask import Blueprint


# initialize login blueprint
login_bp = Blueprint("login", __name__, url_prefix="/login")

# login route
@login_bp.route("", methods=["GET"])
def display_login():
    return "Login here"

# callback route

# logout route