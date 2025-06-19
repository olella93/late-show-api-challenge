from server.config import db
from sqlalchemy.orm import validates

class Appearance(db.Model):
    __tablename__ = "appearances"

    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)

    guest_id = db.Column(db.Integer, db.ForeignKey('guests.id'), nullable=False)
    episode_id = db.Column(db.Integer, db.ForeignKey('episodes.id'), nullable=False)

    guest = db.relationship('Guest', back_populates='appearances')
    episode = db.relationship('Episode', back_populates='appearances')

    @validates('rating')
    def validate_rating(self, key, rating):
        if not 1 <= rating <= 5:
            raise ValueError("Rating must be between 1 and 5.")
        return rating

    def __repr__(self):
        return f"<Appearance Guest={self.guest_id} Episode={self.episode_id} Rating={self.rating}>"
