from flask import Blueprint, request, jsonify
from server.models.episode import Episode
from server.extensions import db

episode_bp = Blueprint('episode_bp', __name__, url_prefix='/episodes')

@episode_bp.route('/', methods=['GET'])
def get_episodes():
    episodes = Episode.query.all()
    episodes_list = [
        {
            "id": episode.id,
            "title": episode.title,
            "air_date": episode.air_date.strftime("%Y-%m-%d")
        }
        for episode in episodes
    ]
    return jsonify(episodes_list), 200

@episode_bp.route('/', methods=['POST'])
def create_episode():
    data = request.get_json()
    new_episode = Episode(title=data['title'], air_date=data['air_date'])
    db.session.add(new_episode)
    db.session.commit()
    return jsonify({
        "id": new_episode.id,
        "title": new_episode.title,
        "air_date": new_episode.air_date.strftime("%Y-%m-%d")
    }), 201

@episode_bp.route('/<int:id>', methods=['GET'])
def get_episode_by_id(id):
    episode = Episode.query.get(id)
    if not episode:
        return jsonify(error="Episode not found"), 404

    appearances_data = [
        {
            "id": appearance.id,
            "rating": appearance.rating,
            "guest": {
                "id": appearance.guest.id,
                "name": appearance.guest.name,
                "occupation": appearance.guest.occupation
            }
        }
        for appearance in episode.appearances
    ]

    return jsonify({
        "id": episode.id,
        "title": episode.title,
        "air_date": episode.air_date.strftime("%Y-%m-%d"),
        "appearances": appearances_data
    }), 200
