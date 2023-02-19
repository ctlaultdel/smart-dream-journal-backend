from app import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
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

    def save(self):
        db.session.add(self)
        db.session.commit()

