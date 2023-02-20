from app import db
from app.models.User import User
from app.models.Entry import Entry
from flask import Blueprint, jsonify, request, abort, make_response
from flask_jwt_extended import get_jwt_identity, jwt_required

# user profile bp
profile_bp = Blueprint("profile", __name__, url_prefix="/profile")

# @jwt_required
# def get_user():
#     user_id = get_jwt_identity()
#     return User.query.filter_by(id=user_id).first()

# user entries routes
@profile_bp.route("/journal/entries", methods=["POST"])
@jwt_required()
def display_user_entries():
    # get user from jwt token
    user_id = get_jwt_identity()
    user = User.query.filter_by(id=user_id).first()
    # create response
    response = []
    for entry in user.entries:
        response.append(entry.to_dict())
    return jsonify(response)

# user new entry route
@profile_bp.route("/journal", methods=["POST"])
@jwt_required()
def create_user_entry():
    # get user from jwt token
    user_id = get_jwt_identity()
    user = User.query.filter_by(id=user_id).first()
    # check request for required attributes
    request_body = request.get_json()
    for attr in ["title", "keywords", "description", "mood"]:
        try:
            request_body[attr]
        except KeyError as e:
            abort(make_response({"message": f"Request body must include {e}"}, 400))
    # create new Entry
    new_entry = Entry(**request_body, user_id=user_id)
    new_entry.save()
    return make_response({"message": "new entry successfully created"}, 201)

# user delete entry route
@profile_bp.route("/journal/<entry_id>", methods=["POST"])
@jwt_required()
def delete_user_entry(entry_id):
    # get user from jwt token
    # user = get_user()
    # get entry from entry id
    # entry = Entry.query.filter_by(user=user, id=entry_id).first()
    # entry.delete()
    return make_response({"message": "entry successfully deleted"}, 201)
