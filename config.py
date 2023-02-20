import os
from dotenv import load_dotenv

load_dotenv

class ApplicationConfig:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLACHEMY_ECHO = True
    JWT_SECRET_KEY = os.environ["JWT_SECRET_KEY"]