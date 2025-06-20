#!./venv/bin/python3
"""
Module to develop a Simple API using Flask.
"""
from flask import Flask, jsonify, request

app = Flask(__name__)
users = {}


@app.route('/', methods=['GET'])
def home():
    """
    Home endpoint that returns a welcome message.
    """
    return "Welcome to the Flask API!"


@app.route('/data', methods=['GET'])
def data():
    """
    Endpoint to return a list of usernames in the dict users
    """
    return jsonify(list(users.keys()))


@app.route('/status', methods=['GET'])
def status():
    """
    Endpoint to check the status of the API.
    """
    return "OK"


@app.route('/users/<username>', methods=['GET'])
def get_user(username):
    """
    Endpoint to return a user's data
    """
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    """
    Endpoint to add a user.
    """
    user_data = request.get_json()
    username = user_data.get('username')

    if not username:
        return jsonify({"error": "Username is required"}), 400

    users[username] = user_data
    return jsonify({"message": "User added", "user": user_data}), 201


if __name__ == '__main__':
    app.run(debug=False)