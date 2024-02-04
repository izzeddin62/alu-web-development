#!/usr/bin/env python3
""" basic flask app"""

from flask import Flask, jsonify, request, abort, make_response, redirect
from auth import Auth

AUTH = Auth()
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
    user = AUTH.register_user(email, password)
    return jsonify({"email": user.email, "message": "user created"})


@app.route('/sessions', methods=['POST'])
def login():
    """login"""
    email = request.form.get("email")
    password = request.form.get("password")
    if AUTH.valid_login(email, password):
        session_id = AUTH.create_session(email)
        if session_id:
            response = make_response(
                    jsonify({"email": email,
                             "session_id": session_id,
                             "message": "logged in"}))
            response.set_cookie('session_id', session_id)
            return response
    abort(401)


@app.route('/sessions', methods=['DELETE'])
def logout():
    """logout"""
    session_id = request.cookies.get("session_id")
    if session_id:
        user = AUTH.get_user_from_session_id(session_id)
        if user:
            AUTH.destroy_session(user.id)
            return redirect('/')
    abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
