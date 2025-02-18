from flask import Flask, jsonify, request


app = Flask(__name__)


# Dictionnaire des utilisateurs
users = {
    "jane": {
        "username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"
    },
    "john": {
        "username": "john", "name": "John", "age": 30, "city": "New York"
    }
}


# Route principale
@app.route('/')
def home():
    return "Welcome to the Flask API!"


# Route pour retourner les usernames
@app.route('/data', methods=['GET'])
def get_users():
    return jsonify(list(users.keys()))


# Route pour vérifier le statut de l'API
@app.route('/status', methods=['GET'])
def status():
    return "OK"


# Route pour obtenir un utilisateur spécifique
@app.route('/users/<username>', methods=['GET'])
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404


# Route pour ajouter un nouvel utilisateur
@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    if not data or 'username' not in data:
        return jsonify({"error": "Username is required"}), 400
    
    username = data['username']
    if username in users:
        return jsonify({"error": "User already exists"}), 409
    
    users[username] = {
        "username": username,
        "name": data.get("name", ""),
        "age": data.get("age", 0),
        "city": data.get("city", "")
    }
    
    return jsonify({
        "message": "User added",
        "user": users[username]
    }), 201

# Exécuter l'application Flask
if __name__ == "__main__":
    app.run(debug=True)
