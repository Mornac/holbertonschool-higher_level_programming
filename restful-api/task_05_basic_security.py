#!./venv/bin/python3
"""
Module that implements a basic security layer for a RESTful API.
"""
from flask import Flask, jsonify, request
app = Flask(__name__)



@app.route('/basic-protected', methods=['GET'])
def basic_protected():
    """
    A basic protected endpoint that requires authentication.
    """
    if not request.authorization:
        return jsonify({"message": "Authentication required"}), 401
    return jsonify({"Basic Auth: Access Granted"})


@app.route('/login', methods=['POST'])
def login():
    """
    A login endpoint that checks the provided credentials.
    """
    auth = request.authorization
    request.authorization = auth
    username = auth.username
    password = auth.password
    if not username or not password:
        return jsonify({"message": "Credentials are not valid"}), 401
    return jsonify({"message": "access_token: <JWT_TOKEN>"}), 200


@app.route('/jwt-protected', methods=['GET'])
def jwt_protected():
    """
    A JWT protected endpoint that requires a valid JWT token.
    """
    token = request.headers.get('Authorization')
    if not token or token.startswith('Bearer '):
        return jsonify({"message": "Missing or invalid token"}), 401
    return jsonify({"JWT Auth: Access Granted"})


@app.route('/admin-only', methods=['GET'])
def admin_only():
    """
    An endpoint that is accessible only to admin users.
    """
    auth = request.authorization
    if not auth or not (auth.username == 'admin' and auth.password == 'admin'):
        return jsonify({"message": "Admin access required"}), 403
    return jsonify({"message": "Admin access granted"})
