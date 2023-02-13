from flask import Blueprint

# initialize calendar blueprint
calendar_bp = Blueprint("calendar", __name__, url_prefix="/calendar")

# calendar route
@calendar_bp.route("", methods=["GET"])
def display_calendar():
    return "Calendar Here"