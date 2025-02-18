#!/usr/bin/env python3
from flask import Flask, jsonify, request

app = Flask(__name__)

users = {
    "jane": {"name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"name": "John", "age": 30, "city": "New York"}
}

@app.route("/")
def home():
    return "Welcome to the Flask API!"

@app.route("/data", methods=["GET"])
def get_data():
    return jsonify(list(users.keys()))

@app.route("/status", methods=["GET"])
def get_status():
    return "OK"

@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    if username in users:
        user_data = users[username].copy()
        user_data["username"] = username
        return jsonify(user_data)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.get_json()
    
    if not data or "username" not in data:
        return jsonify({"error": "Username is required"}), 400
    
    username = data["username"]
    users[username] = {
        "name": data.get("name", ""),
        "age": data.get("age", 0),
        "city": data.get("city", "")
    }

    user_data = users[username].copy()
    user_data["username"] = username

    return jsonify({
        "message": "User added",
        "user": user_data
    }), 201

if __name__ == "__main__":
    app.run()
