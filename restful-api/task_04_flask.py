#!/usr/bin/env python3
"""
Module to develop a Simple API using Flask.
"""
import json
from flask import Flask, jsonify, request
app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    """
    Home endpoint that returns a welcome message.
    """
    return "Welcome to the Flask API!"


def users(self):
    pass


@app.route('/data', methods=['GET'])
def data(self):
    """
    Endpoint to return a list of usernames in the dict users
    """
    requests.get()
    jsonify(json.dumps(__dict__))


@app.route('/status', methods=['GET'])
def status(self):
    """
    Endpoint to check the status of the API.
    """
    self.send_response(200)
    self.send_header('Content-Type', 'text/plain')
    self.end_headers()
    self.wfile.write(b'OK')
    json.dumps({"status": "OK"})
    self.path = '/status'


@app.route('/users/<username>')
def users():
    """
    Endpoint to return the user
    """
    return users


@app.route('/add_user', methods=['POST'])
def add_user():
    """
    Endpoint to add a user.
    """
    data = request.get_json()
    if not data or 'user' not in data:
        return jsonify({"error": "Username is required"}), 400


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000)
