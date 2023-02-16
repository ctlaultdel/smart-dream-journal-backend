from app import db
from datetime import date

class Entry(db.Model):
    __tablename__ = "entries"
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, default=date.today())
    title = db.Column(db.String)
    keywords = db.Column(db.String, nullable=False)
    description = db.Column(db.Text)
    mood = db.Column(db.String, nullable=False)
    user = db.relationship("User", back_populates="entries")
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def to_dict(self):
        """
        Returns dictionary of entry data
        """
        return {
            "id": self.id,
            "date": self.date,
            "title": self.title,
            "keywords": self.keywords,
            "description": self.description,
            "mood": self.mood,
            "user_id": self.user_id
        }

    @classmethod
    def from_dict(cls, dict):
        return Entry(
            title=dict["title"],
            keywords=dict["keywords"],
            description=dict["description"],
            mood=dict["mood"],
        )