from flask import Blueprint, jsonify
from server.models.guest import Guest

guest_bp = Blueprint('guest_bp', __name__, url_prefix='/guests')

@guest_bp.route('/', methods=['GET'])
def get_guests():
    guests = Guest.query.all()
    guests_data = [
        {
            "id": guest.id,
            "name": guest.name,
            "occupation": guest.occupation
        }
        for guest in guests
    ]
    return jsonify(guests_data), 200
