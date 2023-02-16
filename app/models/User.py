from app import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)
    entries = db.relationship("Entry", back_populates="user")

    @classmethod
    def from_dict(cls, dict):
        return User(username=dict["username"],
            password=dict["password"])
    
    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "password": self.password,
            "entries": self.entries
        }