from flask import Blueprint

# initialize analyses blueprint
analyses_bp = Blueprint("analyses", __name__, url_prefix="/analyses")

# analyses route
@analyses_bp.route("", methods=["GET"])
def display_analyses():
    return "Analyses here"