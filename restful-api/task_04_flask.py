"""A simple Flask API implementation"""
import flask

app = flask.Flask(__name__)

# Store users in memory
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
    """Root endpoint"""
    return "Welcome to the Flask API!"


@app.route('/data')
def get_data():
    """Return list of all usernames"""
    return flask.jsonify(list(users.keys()))


@app.route('/status')
def get_status():
    """Return API status"""
    return "OK"


@app.route('/users/<username>')
def get_user(username):
    """Return user data for given username"""
    if username in users:
        return flask.jsonify(users[username])
    return flask.jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    """Add a new user"""
    data = flask.request.get_json()

    # Check if username is provided
    if 'username' not in data:
        return flask.jsonify({"error": "Username is required"}), 400

    # Create new user entry with username included
    username = data['username']
    new_user = {
        "username": username,
        "name": data.get('name'),
        "age": data.get('age'),
        "city": data.get('city')
    }

    # Add user to dictionary
    users[username] = new_user

    # Return success response with exact format
    return flask.jsonify({
        "message": "User added",
        "user": new_user
    }), 201


if __name__ == '__main__':
    app.run(port=5000)
