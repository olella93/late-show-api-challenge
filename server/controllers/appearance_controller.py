from flask import Blueprint, request, jsonify
from server.models.appearance import Appearance
from server.models import db

appearance_bp = Blueprint('appearance_bp', __name__, url_prefix='/appearances')

@appearance_bp.route('/', methods=['GET'])
def get_appearances():
    appearances = Appearance.query.all()
    return jsonify([appearance.to_dict() for appearance in appearances]), 200

@appearance_bp.route('/', methods=['POST'])
def create_appearance():
    data = request.get_json()
    new_appearance = Appearance(
        rating=data['rating'],
        guest_id=data['guest_id'],
        episode_id=data['episode_id']
    )
    db.session.add(new_appearance)
    db.session.commit()
    return jsonify(new_appearance.to_dict()), 201
