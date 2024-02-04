#!/usr/bin/env python3
""" basic flask app"""

from flask import Flask, jsonify, request
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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
