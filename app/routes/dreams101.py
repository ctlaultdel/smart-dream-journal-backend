from flask import Blueprint

# initialize dreams101 blueprint
dreams101_bp = Blueprint("dreams101", __name__, url_prefix="/dreams101")

# dreams101 route
@dreams101_bp.route("", methods=["GET"])
def display_dreams101_facts():
    return "Display dreams101 here"