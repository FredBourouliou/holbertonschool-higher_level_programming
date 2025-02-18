"""A simple Flask API implementation"""
from flask import Flask, jsonify, request

app = Flask(__name__)

# Stockage en mémoire des utilisateurs
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


@app.route('/', methods=['GET'])
def home():
    """Page d'accueil"""
    return app.response_class(
        response="Welcome to the Flask API!",
        status=200,
        mimetype="text/plain"
    )


@app.route('/data', methods=['GET'])
def get_data():
    """Retourne une liste des usernames"""
    return jsonify(list(users.keys())), 200


@app.route('/status', methods=['GET'])
def get_status():
    """Renvoie OK en texte brut"""
    return app.response_class(
        response="OK",
        status=200,
        mimetype="text/plain"
    )


@app.route('/users/<username>', methods=['GET'])
def get_user(username):
    """Retourne les informations d'un utilisateur spécifique"""
    user = users.get(username)
    if user:
        return jsonify(user), 200
    return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    """Ajoute un nouvel utilisateur"""
    if not request.is_json:
        return jsonify({"error": "Invalid JSON format"}), 400

    data = request.get_json()

    if "username" not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data["username"]

    if username in users:
        return jsonify({"error": "User already exists"}), 400

    # Assurer que tous les champs existent (éviter None)
    new_user = {
        "username": username,
        "name": data.get("name", ""),
        "age": data.get("age", 0),
        "city": data.get("city", "")
    }

    users[username] = new_user

    return jsonify({
        "message": "User added",
        "user": new_user
    }), 201


if __name__ == '__main__':
    app.run(debug=True)