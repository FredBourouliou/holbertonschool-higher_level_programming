#!/usr/bin/env python3
"""
A simple Flask API example based on the given instructions.
"""

from flask import Flask, request, jsonify

app = Flask(__name__)

# Exemple de données initiales
# Chaque valeur du dictionnaire contient déjà le champ "username"
users = {
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
}

@app.route("/")
def home():
    """
    Endpoint racine ("/"): doit retourner la chaîne de caractères "Welcome to the Flask API!".
    """
    return "Welcome to the Flask API!"

@app.route("/data")
def get_data():
    """
    Endpoint "/data": retourne en JSON la liste des usernames.
    Exemple: ["jane", "john"]
    """
    # On retourne uniquement la liste des clés du dictionnaire users
    return jsonify(list(users.keys()))

@app.route("/status")
def status():
    """
    Endpoint "/status": doit retourner la chaîne de caractères "OK".
    """
    return "OK"

@app.route("/users/<username>")
def get_user(username):
    """
    Endpoint "/users/<username>": retourne l'objet complet associé au username si trouvé,
    sinon un JSON {"error": "User not found"} avec un code 404.
    """
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404

@app.route("/add_user", methods=["POST"])
def add_user():
    """
    Endpoint "/add_user": accepte des requêtes POST contenant des données JSON.
    Exemples de données JSON attendues:
        {
            "username": "alice",
            "name": "Alice",
            "age": 25,
            "city": "San Francisco"
        }
    
    1) Si le champ "username" est manquant, on retourne un code 400 et un JSON: {"error": "Username is required"}.
    2) Sinon, on ajoute l'utilisateur dans le dictionnaire 'users' puis on retourne un code 201 et
       un JSON confirmant l'ajout, par exemple:
       {
           "message": "User added",
           "user": {
               "username": "alice",
               "name": "Alice",
               "age": 25,
               "city": "San Francisco"
           }
       }
    """
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400

    if "username" not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data["username"]
    # On insère/écrase simplement l'utilisateur (selon la logique voulue)
    users[username] = data
    return jsonify({"message": "User added", "user": data}), 201

# Point d'entrée pour exécuter le serveur Flask en mode développement
if __name__ == "__main__":
    app.run()