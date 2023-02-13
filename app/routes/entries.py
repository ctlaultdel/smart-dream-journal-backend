from flask import Blueprint

# initialize entries blueprint
entries_bp = Blueprint("entries", __name__, url_prefix="/entries")

# entries route
@entries_bp.route("", methods=["GET"])
def display_entries():
    return "Dream Journal Entries"