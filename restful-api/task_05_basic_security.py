#!/usr/bin/python3
"""A secure Flask API implementation with Basic Auth and JWT"""
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    JWTManager, create_access_token, get_jwt_identity,
    jwt_required
)

app = Flask(__name__)
auth = HTTPBasicAuth()

# Setup JWT
app.config['JWT_SECRET_KEY'] = 'super-secret-key'  # Change this in production!
jwt = JWTManager(app)

# Store users in memory with hashed passwords
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


@auth.verify_password
def verify_password(username, password):
    """Verify user credentials for basic auth"""
    if username in users and check_password_hash(
            users[username]["password"], password):
        return username
    return None


@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    """Basic auth protected endpoint"""
    return "Basic Auth: Access Granted"


@app.route('/login', methods=['POST'])
def login():
    """Login endpoint to get JWT token"""
    data = request.get_json()

    if not data or 'username' not in data or 'password' not in data:
        return jsonify({"error": "Missing username or password"}), 401

    username = data['username']
    password = data['password']

    if username in users and check_password_hash(
            users[username]["password"], password):
        # Create token with role in identity
        access_token = create_access_token(
            identity={
                "username": username,
                "role": users[username]["role"]
            }
        )
        return jsonify({"access_token": access_token})

    return jsonify({"error": "Invalid credentials"}), 401


@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    """JWT protected endpoint"""
    return "JWT Auth: Access Granted"


@app.route('/admin-only')
@jwt_required()
def admin_only():
    """Admin-only endpoint"""
    current_user = get_jwt_identity()
    if current_user.get("role") != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"

# JWT error handlers


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """Handle missing JWT token"""
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """Handle invalid JWT token"""
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(header, payload):
    """Handle expired JWT token"""
    return jsonify({"error": "Token has expired"}), 401


if __name__ == '__main__':
    app.run(port=5000)
