from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from server.models.appearance import Appearance
from server.models.episode import Episode
from server.models.guest import Guest
from server.extensions import db

appearance_bp = Blueprint('appearance_bp', __name__, url_prefix='/appearances')

@appearance_bp.route('/', methods=['POST'])
@jwt_required()
def create_appearance():
    data = request.get_json()

    # Validate required fields
    required_fields = ['rating', 'guest_id', 'episode_id']
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing field: {field}"}), 400

    # Check if guest and episode exist
    guest = Guest.query.get(data['guest_id'])
    episode = Episode.query.get(data['episode_id'])

    if not guest or not episode:
        return jsonify({"error": "Invalid guest_id or episode_id"}), 404

    # Create and save appearance
    new_appearance = Appearance(
        rating=data['rating'],
        guest_id=data['guest_id'],
        episode_id=data['episode_id']
    )
    db.session.add(new_appearance)
    db.session.commit()

    return jsonify({
        "id": new_appearance.id,
        "rating": new_appearance.rating,
        "episode": {
            "id": episode.id,
            "title": episode.title
        },
        "guest": {
            "id": guest.id,
            "name": guest.name
        }
    }), 201
