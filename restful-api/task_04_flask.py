#!/usr/bin/env python3
from flask import Flask, jsonify, request

app = Flask(__name__)

# Dictionnaire en mémoire, avec "username" comme clé
# et un objet contenant toutes les infos de l'utilisateur comme valeur.
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

@app.route("/")
def home():
    # 1) Le chemin "/" doit renvoyer le message :
    # "Welcome to the Flask API!"
    return "Welcome to the Flask API!"

@app.route("/data", methods=["GET"])
def get_data():
    # 2) Le chemin "/data" doit renvoyer la liste de tous les usernames
    # existants dans la variable users.
    # Format attendu : ["jane", "john"]
    return jsonify(list(users.keys()))

@app.route("/status", methods=["GET"])
def get_status():
    # 3) Le chemin "/status" renvoie la chaîne de caractère "OK"
    return "OK"

@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    # 4) Le chemin "/users/<username>" renvoie l'objet complet correspondant
    # à l'utilisateur, ex. :
    # {
    #   "username": "jane", 
    #   "name": "Jane",
    #   "age": 28,
    #   "city": "Los Angeles"
    # }
    # S'il n'existe pas, renvoyer {"error": "User not found"} avec un code 404.
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404

@app.route("/add_user", methods=["POST"])
def add_user():
    # 5) Le chemin "/add_user" doit accepter des requêtes POST.
    # On récupère les données JSON envoyées.
    data = request.get_json()
    if not data:
        # Si aucun JSON n'est envoyé, on peut considérer que 'username'
        # est absent, donc on renvoie une erreur 400.
        return jsonify({"error": "Username is required"}), 400
    
    # On vérifie la présence du champ 'username'
    if "username" not in data:
        return jsonify({"error": "Username is required"}), 400
    
    username = data["username"]
    name = data.get("name", "")
    age = data.get("age", 0)
    city = data.get("city", "")

    # On ajoute le nouvel utilisateur dans la variable users
    # (On peut éventuellement gérer le cas où l’utilisateur existe déjà,
    #  mais ça n'est pas précisé dans la consigne.)
    users[username] = {
        "username": username,
        "name": name,
        "age": age,
        "city": city
    }

    # Conformément aux spécifications :
    #  - renvoyer un code 201 (Created)
    #  - renvoyer un message de confirmation et les données de l'utilisateur ajouté
    return jsonify({
        "message": "User added",
        "user": users[username]
    }), 201

if __name__ == "__main__":
    # Démarre le serveur Flask
    app.run()