import logging

from flask import Flask, jsonify, request

from db import DBConnection
from model import User

app = Flask(__name__)


@app.route("/api/v1/health-check")
def health_check():
    return "<p>I am working...</p>"


@app.route('/', methods=['GET'])
def hello():
    return 'Hello, World'


@app.route('/api/v1/users', methods=['GET'])
def get_all_users():
    try:
        db = DBConnection()
        status, response, message, status_code = db.get_users()
        return jsonify({"status": status, "data": response, "message": message}), status_code
    except Exception as error:
        logging.exception(f"Failed to get users with error {error}")
        return jsonify({"status": False, "data": None, "message": f"Failed to get users with error {error}"}), 500


@app.route('/api/v1/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    try:
        db = DBConnection()
        status, response, message, status_code = db.get_user(user_id)
        return jsonify({"status": status, "data": response, "message": message}), status_code
    except Exception as error:
        logging.exception(f"Failed to get user details with error {error}")
        return jsonify({"status": False, "data": None, "message": f"Failed to get user details with error {error}"}), 500


@app.route('/api/v1/users', methods=['POST'])
def create_user():
    try:
        data = request.json
        name = data.get('name')
        email = data.get('email')
        age = data.get('age')
        status = data.get('status')
        if not name or not email or not age:
            return jsonify({"status": False, "data": None, "message": "Missing required fields"}), 400
        user = User(name, email, age, status)
        db = DBConnection()
        api_status, response, message, status_code = db.create_user(user)
        return jsonify({"status": api_status, "data": response, "message": message}), status_code
    except Exception as error:
        logging.exception(f"Failed to create user with error {error}")
        return jsonify({"status": False, "data": None, "message": f"Failed to create user with error {error}"}), 500


@app.route('/api/v1/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    try:
        data = request.json
        name = data.get('name')
        email = data.get('email')
        age = data.get('age')
        status = data.get('status')
        if not name or not email or not age or not status:
            return 'Missing required fields', 400
        user = User(name, email, age,status)
        db = DBConnection()
        u_status, u_response, u_message, u_status_code = db.update_user(user_id, user)
        return jsonify({"status": u_status, "data": u_response, "message": u_message}), u_status_code
    except Exception as error:
        logging.exception(f"Failed to update user with error {error}")
        return jsonify({"status": False, "data": None, "message": f"Failed to update user with error {error}"}), 500


@app.route('/api/v1/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    try:
        db = DBConnection()
        d_status, d_response, d_message, d_status_code = db.delete_user(user_id)
        return jsonify({"status": d_status, "data": d_response, "message": d_message}), d_status_code
    except Exception as error:
        logging.exception(f"Failed to delete user with error {error}")
        return jsonify({"status": False, "data": None, "message": f"Failed to delete user with error {error}"}), 500


if __name__ == '__main__':
    db = DBConnection()
    db.create_tables()
    app.run()
