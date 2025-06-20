from flask import Blueprint, request, jsonify
from server.models.user import User
from server.extensions import db
from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash

auth_bp = Blueprint('auth_bp', __name__)

# Register route
@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not username or not email or not password:
        return jsonify(error="All fields are required."), 400

    if User.query.filter((User.username == username) | (User.email == email)).first():
        return jsonify(error="Username or email already taken."), 400

    user = User(username=username, email=email)
    user.password_hash = password  

    db.session.add(user)
    db.session.commit()

    token = create_access_token(identity=user.id)
    return jsonify(access_token=token), 201

# Login route
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify(error="Username and password required."), 400

    user = User.query.filter_by(username=username).first()

    if user and user.authenticate(password):
        token = create_access_token(identity=user.id)
        return jsonify(access_token=token), 200

    return jsonify(error="Invalid credentials."), 401
