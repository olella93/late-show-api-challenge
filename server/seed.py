from server.app import create_app, db
from server.models.user import User
from server.models.guest import Guest
from server.models.episode import Episode
from server.models.appearance import Appearance
from werkzeug.security import generate_password_hash

app = create_app()

with app.app_context():
    # Clear all tables
    print("Clearing old data...")
    db.drop_all()
    db.create_all()

    # Seed Users
    user1 = User(
        username="admin",
        email="admin@example.com",
        password_hash=generate_password_hash("adminpass")
    )

    # Seed Guests
    guest1 = Guest(name="Ziwe", occupation="Comedian")
    guest2 = Guest(name="John Doe", occupation="Actor")

    # Seed Episodes
    episode1 = Episode(title="Episode 1", air_date="2024-05-01")
    episode2 = Episode(title="Episode 2", air_date="2024-05-08")

    # Seed Appearances
    appearance1 = Appearance(guest=guest1, episode=episode1)
    appearance2 = Appearance(guest=guest2, episode=episode2)

    # Add all to session
    db.session.add_all([user1, guest1, guest2, episode1, episode2, appearance1, appearance2])
    db.session.commit()

    print("🌱 Seeded successfully!")
