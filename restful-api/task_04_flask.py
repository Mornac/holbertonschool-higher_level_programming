#!/usr/bin/env python3
"""
Module to develop a Simple API using Flask.
"""
import json
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
    return jsonify({"status": "OK"}), 200


@app.route('/users/<username>', methods=['GET'])
def get_user(username):
    """
    Endpoint to return the user
    """
    user = users.get(username)
    if user:
        return jsonify(user), 200
    else:
        return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    """
    Endpoint to add a user.
    """
    data = request.get_json()

    if not data or 'username' not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data['username']

    if username in users:
        return jsonify({"error": "Username already exists"}), 400

    users[username] = data
    return jsonify({"message": f"User {username} added successfully"}), 201


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000)
