from .User import User
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
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

class RegisterForm(FlaskForm):
    username = StringField(
        validators=[InputRequired(), Length(min=4, max=20)], 
        render_kw={"placeholder": "Username"})
    password = PasswordField(
        validators=[InputRequired(), Length(min=4, max=80)],
        render_kw={"placeholder": "Password"})
    submit = SubmitField("Register")

    def validate_username(self, username):
        existing_username = User.query.filter_by(
            username = username.data).first()
        if existing_username:
            raise ValidationError(
                "Username already exists. Please choose a different username."
            )
        
class LoginForm(FlaskForm):
    username = StringField(
        validators=[InputRequired(), Length(min=4, max=20)], 
        render_kw={"placeholder": "Username"})
    password = PasswordField(
        validators=[InputRequired(), Length(min=4, max=80)],
        render_kw = {"placeholder": "Password"})
    
    submit = SubmitField("Login")