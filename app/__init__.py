from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

# db initialization
db = SQLAlchemy()
migrate = Migrate(compare_type=True)
load_dotenv()

def create_app(test_config=None):
    app = Flask(__name__)
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # select development or testing db
    if test_config:
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("SQLALCHEMY_TEST_DATABASE_URI")
        app.config["TESTING"] = True
    else:
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("SQLALCHEMY_DATABASE_URI")

    # import models
    from app.models.Entry import Entry

    # setup db
    db.init_app(app)
    migrate.init_app(app, db)

    # register blueprints
    from app.routes.login_routes import login_bp
    from app.routes.entries import entries_bp
    from app.routes.dreams101 import dreams101_bp
    from app.routes.calendar import calendar_bp
    from app.routes.analyses import analyses_bp
    app.register_blueprint(login_bp)
    app.register_blueprint(entries_bp)
    app.register_blueprint(dreams101_bp)
    app.register_blueprint(calendar_bp)
    app.register_blueprint(analyses_bp)
    
    return app