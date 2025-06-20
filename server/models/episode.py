from server.extensions import db

class Episode(db.Model):
    __tablename__ = "episodes"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    air_date = db.Column(db.Date, nullable=False)

    appearances = db.relationship('Appearance', back_populates='episode', cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Episode {self.title} - {self.air_date}>"
