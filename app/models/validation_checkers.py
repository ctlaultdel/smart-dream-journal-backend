from .User import User
from flask import abort, make_response

def validate_model(cls, model_id):
    try:
        model_id = int(model_id)
    except:
        # handle invalid entry id type
        abort(make_response({"message":f"{cls.__name__} {model_id} invalid"}, 400))
    # return entry data if id in db
    model = cls.query.get(model_id)
    # handle nonexistant planet id
    if not model:
        abort(make_response({"message":f"{cls.__name__} {model_id} not found"}, 404))
    return model