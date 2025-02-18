"""A RESTful API implementation using Flask

This module demonstrates the basic concepts of REST APIs:
- HTTP methods (GET, POST)
- Resource-based routing
- JSON data handling
- Status codes
"""
from flask import Flask, jsonify, request

# Initialize Flask application
app = Flask(__name__)

# In-memory database simulation
users = {
    "jane": {
        "username": "jane",
        "name": "Jane",
        "age": 28,
        "city": "Los Angeles"
    },
    "john": {
        "username": "john",
        "name": "John",
        "age": 30,
        "city": "New York"
    }
}


@app.route('/')
def home():
    """Root endpoint
    
    Returns:
        str: Welcome message
    """
    return "Welcome to the Flask API!"


@app.route('/data')
def get_data():
    """List all resources (usernames)
    
    Returns:
        JSON: List of available usernames
    """
    return jsonify(list(users.keys()))


@app.route('/status')
def get_status():
    """Health check endpoint
    
    Returns:
        str: API status
    """
    return "OK"


@app.route('/users/<username>')
def get_user(username):
    """Retrieve a specific user's data
    
    Args:
        username (str): The username to look up
    
    Returns:
        JSON: User data or error message
    """
    if username in users:
        return jsonify(users[username])
    return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    """Create a new user
    
    Expected JSON payload:
    {
        "username": "alice",
        "name": "Alice",
        "age": 25,
        "city": "San Francisco"
    }
    
    Returns:
        JSON: Confirmation message and user data
    """
    data = request.get_json()

    if not data or 'username' not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data['username']
    new_user = {
        "username": username,
        "name": data.get('name'),
        "age": data.get('age'),
        "city": data.get('city')
    }

    users[username] = new_user

    return jsonify({
        "message": "User added",
        "user": new_user
    }), 201


if __name__ == '__main__':
    app.run()