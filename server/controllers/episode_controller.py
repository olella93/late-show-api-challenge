from flask import Blueprint, request, jsonify
from server.models.episode import Episode
from server.models import db

episode_bp = Blueprint('episode_bp', __name__, url_prefix='/episodes')

@episode_bp.route('/', methods=['GET'])
def get_episodes():
    episodes = Episode.query.all()
    return jsonify([episode.to_dict() for episode in episodes]), 200

@episode_bp.route('/', methods=['POST'])
def create_episode():
    data = request.get_json()
    new_episode = Episode(date=data['date'], title=data['title'])
    db.session.add(new_episode)
    db.session.commit()
    return jsonify(new_episode.to_dict()), 201
