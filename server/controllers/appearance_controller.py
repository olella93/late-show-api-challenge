from flask import Blueprint

appearance_bp = Blueprint('appearance_bp', __name__)

@appearance_bp.route("/appearances", methods=["GET"])
def get_appearances():
    return {"message": "Placeholder for appearances"}
