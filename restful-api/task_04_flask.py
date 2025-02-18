import json
from flask import Flask, jsonify, request

app = Flask(__name__)

# Dictionnaire d'utilisateurs en mémoire
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
    """Retourne un message d'accueil."""
    return "Welcome to the Flask API!"

@app.route('/data', methods=['GET'])
def get_data():
    """
    Retourne la liste de tous les usernames
    sous forme de JSON (ex. ["jane","john"]).
    """
    return jsonify(list(users.keys()))

@app.route('/status', methods=['GET'])
def status():
    """Retourne 'OK'."""
    return "OK"

@app.route('/users/<username>', methods=['GET'])
def get_user(username):
    """
    Retourne les informations de l'utilisateur <username>.
    Si l'utilisateur n'existe pas, renvoie:
      {"error": "User not found"} avec un code 404.
    """
    if username in users:
        return jsonify(users[username])
    return jsonify({"error": "User not found"}), 404

@app.route('/add_user', methods=['POST'])
def add_user():
    """
    Attend un JSON de la forme:
      {
        "username": "alice",
        "name": "Alice",
        "age": 25,
        "city": "San Francisco"
      }
    - Si 'username' est absent, renvoie un code 400:
        {"error": "Username is required"}
    - Sinon, ajoute l'utilisateur et renvoie un code 201:
        {
          "message": "User added",
          "user": { ... }
        }
    """
    data = request.get_json()

    # Vérifie l'absence des données ou du champ 'username'
    if not data or "username" not in data:
        return jsonify({"error": "Username is required"}), 400

    # Ajoute ou écrase l'utilisateur dans le dictionnaire
    users[data["username"]] = data

    return jsonify({
        "message": "User added",
        "user": data
    }), 201

if __name__ == '__main__':
    # Lance le serveur Flask
    app.run()