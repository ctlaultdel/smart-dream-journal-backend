import os
from dotenv import load_dotenv

load_dotenv

class ApplicationConfig:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLACHEMY_ECHO = True