from flask import Flask, request, jsonify

app = Flask(__name__)

# Dictionnaire d'exemple avec deux utilisateurs au démarrage
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
    return "Welcome to the Flask API!"

@app.route("/data")
def get_data():
    # Retourne la liste de tous les usernames
    return jsonify(list(users.keys()))

@app.route("/status")
def status():
    return "OK"

@app.route("/users/<username>")
def get_user(username):
    # Vérifie si le username existe dans le dictionnaire
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404

@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.get_json()

    # Vérifie la présence du champ "username"
    if "username" not in data:
        return jsonify({"error": "Username is required"}), 400

    # Ajoute (ou remplace) l'utilisateur dans le dictionnaire
    users[data["username"]] = data

    # Retourne un code 201 et un message de confirmation avec les données de l'utilisateur
    return jsonify({
        "message": "User added",
        "user": data
    }), 201

if __name__ == "__main__":
    app.run()