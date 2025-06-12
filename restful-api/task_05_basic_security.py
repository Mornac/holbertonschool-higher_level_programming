#!./venv/bin/python3
"""
Module that implements a basic security layer for a RESTful API.
"""
from webbrowser import get
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth, HTTPDigestAuth
from werkzeug.security import generate_password_hash, check_password_hash
app = Flask(__name__)
auth = HTTPBasicAuth()
app.config['SECRET_KEY'] = 'secret_key'
auth = HTTPDigestAuth()
auth = HTTPTokenAuth()


users = {
    "user": generate_password_hash("password"),
    "admin": generate_password_hash("admin")
}

tokens = {
    "user_token1": "user_token_value",
    "admin_token1": "admin_token_value"
}


"""
@auth.verify_password
def verify_password(username, password):
    
    Verify the username and password against stored credentials.
    
    if username in users and \
            check_password_hash(users.get(username), password):
        return username
"""


@app.route('/')
@auth.login_required
def index():
    """
    A simple index endpoint that returns a welcome message.
    """
    return jsonify({"message": "Welcome to the RESTful API with Basic Security"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


@auth.get_password
def get_password(username):
    """
    Get the password for a given username.
    """
    if username in users:
        return users.get(username)
    return None


@app.route('/')
@auth.login_required
def index():
    """
    A home endpoint that requires authentication.
    """
    return jsonify({"message": "Welcome to the Home Page"})


@auth.verify_token
def verify_token(token):
    """
    Verify the token against stored tokens.
    """
    if token in tokens:
        return tokens.get(token)
    return None


@app.route('/')
@auth.login_required
def index():
    """
    A home endpoint that requires token authentication.
    """
    return jsonify({"message": "Welcome to the Home Page with Token Authentication"})


@auth.get_user_roles
def get_user_roles(username):
    """
    Get the roles for a given username.
    """
    if username == 'admin':
        return ['admin']
    return ['user']


@app.route('/admin', methods=['GET'])
@auth.login_required(role='admin')  
def admin():
    """
    An admin endpoint that requires authentication.
    """
    if not request.authorization or not (request.authorization.username == 'admin' and request.authorization.password == 'admin'):
        return jsonify({"message": "Admin access required"}), 403
    return jsonify({"message": "Admin access granted"})


@auth.hash_password
def hash_password(password):
    """
    Hash the provided password.
    """
    return hash_password(password)


@app.route('/basic-protected', methods=['GET'])
def basic_protected():
    """
    A basic protected endpoint that requires authentication.
    """
    request.authorization = HTTPBasicAuth().authenticate(request)
    get().auth().basic("your username", "your password").get("your end point URL")
    generate_password_hash("your password")
    check_password_hash("your hashed password", "your password")
    if not request.authorization or not (request.authorization.username == 'user' and request.authorization.password == 'password'):
        return jsonify({"message": "Authentication required"}), 401
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
