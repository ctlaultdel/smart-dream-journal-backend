from flask import Blueprint, jsonify, request, make_response
from app import db
from app.models.Entry import Entry
from app.models.validation_checkers import validate_model

# initialize entries blueprint
entries_bp = Blueprint("journal", __name__, url_prefix="/journal")

# all entries route
@entries_bp.route("", methods=["GET"])
def display_entries():
    entries = Entry.query.all()
    response = []
    for entry in entries:
        response.append(entry.to_dict())
    return jsonify(response)

# single entry route
@entries_bp.route("/<entry_id>", methods=["GET"])
def display_one_entry(entry_id):
    entry = validate_model(Entry, entry_id)
    return entry.to_dict()

# post new entry route
@entries_bp.route("", methods=["POST"])
def create_new_entry():
    request_body = request.get_json()
    new_entry = Entry.from_dict(request_body)
    db.session.add(new_entry)
    db.session.commit()
    return make_response({
        "message": "new dream entry successfully logged"
    }, 201)
