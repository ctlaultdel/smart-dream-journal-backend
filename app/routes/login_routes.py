from flask import Blueprint
from app.models.validation_checkers import LoginForm, RegisterForm


# initialize blueprints
main_bp = Blueprint("main", __name__, url_prefix="/")
@main_bp.route("", methods=["GET"])
def display_homepage():
    return "Main page"

# login route
login_bp = Blueprint("login", __name__, url_prefix="/login")
@login_bp.route("", methods=["GET", "POST"])
def display_login():
    form = LoginForm()
    return form

# register route
register_bp = Blueprint("register", __name__, url_prefix="/register")
@register_bp.route("", methods=["GET", "POST"])
def register_user():
    form = RegisterForm()
    return form
# callback route

# logout route