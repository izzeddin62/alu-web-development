#!/usr/bin/env python3
""" basic flask app"""

from flask import Flask, jsonify, request, abort, make_response
from auth import Auth

auth = Auth()
app = Flask(__name__)

app.url_map.strict_slashes = False


@app.route('/')
def hello_world():
    """hello world"""
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'])
def register_user():
    """register user"""
    email = request.form.get("email")
    password = request.form.get("password")
    user = auth.register_user(email, password)
    return jsonify({"email": user.email, "message": "user created"})


@app.route('/sessions', methods=['POST'])
def login():
    """login"""
    email = request.form.get("email")
    password = request.form.get("password")
    if auth.valid_login(email, password):
        session_id = auth.create_session(email)
        if session_id:
            response = make_response(
                    jsonify({"email": email, "session_id": session_id}))
            response.set_cookie('session_id', session_id)
            return response
    abort(401)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
