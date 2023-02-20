from app import db
from datetime import date

class Entry(db.Model):
    __tablename__ = "entries"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.Date, default=date.today())
    title = db.Column(db.String, nullable=False)
    keywords = db.Column(db.String, nullable=False)
    description = db.Column(db.Text, nullable=False)
    mood = db.Column(db.String, nullable=False)
    user = db.relationship("User", back_populates="entries")
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def to_dict(self):
        """
        Returns dictionary of entry data
        """
        return {
            "date": self.date,
            "title": self.title,
            "keywords": self.keywords,
            "description": self.description,
            "mood": self.mood,
        }

    @classmethod
    def from_dict(cls, dict, user):
        return Entry(
            title=dict["title"],
            keywords=dict["keywords"],
            description=dict["description"],
            mood=dict["mood"],
            user=user,
            user_id=user.id,
            )
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
