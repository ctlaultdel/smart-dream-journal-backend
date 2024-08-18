from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import ApplicationConfig
from flask_jwt_extended import JWTManager
import os

# db initialization
db = SQLAlchemy()
migrate = Migrate(compare_type=True)

def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_object(ApplicationConfig)
    
    CORS(app)
    jwt = JWTManager(app)
    app.config['CORS_HEADERS'] = 'Content-Type'

    # select development or testing db
    if test_config:
        app.config["SQLALCHEMY_DATABASE_URI"] =os.environ.get("SQLALCHEMY_TEST_DATABASE_URI")
        app.config["TESTING"] = True
    else:
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("SQLALCHEMY_DATABASE_URI")

    # import models for Alembic setup
    from app.models.Entry import Entry
    from app.models.User import User

    # setup db
    db.init_app(app)
    migrate.init_app(app, db)

    # register blueprints
    from app.routes.auth import auth_bp
    from app.routes.profile import profile_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(profile_bp)

    return app