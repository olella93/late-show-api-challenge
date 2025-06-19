from flask import Blueprint

guest_bp = Blueprint('guest_bp', __name__)

@guest_bp.route("/guests", methods=["GET"])
def get_guests():
    return {"message": "Placeholder route for guests"}
