from server.config import db

class Episode(db.Model):
    __tablename__ = "episodes"

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    number = db.Column(db.Integer, nullable=False)

    appearances = db.relationship('Appearance', back_populates='episode', cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Episode {self.number} - {self.date}>"
