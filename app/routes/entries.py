from flask import Blueprint, jsonify, request, make_response, abort
from app import db
from app.models.User import User
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
def create_entry():
    request_body = request.get_json()
    attr_reqs = ["title", "keywords", "description", "mood", "user_id"]
    for req in attr_reqs:
        if req not in request_body:
            abort(make_response({
                "message": f"Failed to create a user because {req} missing"
            }, 400))
    user = validate_model(User, request_body["user_id"])
    new_entry = Entry.from_dict(request_body, user)
    db.session.add(new_entry)
    db.session.commit()
    return make_response({
        "message": "new dream entry successfully logged"
    }, 201)
