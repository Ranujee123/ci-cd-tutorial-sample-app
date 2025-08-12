from flask import json, jsonify
from app import app
from app import db
from app.models import Menu

@app.route('/')
def home():
	return jsonify({ "status": "hello" })

@app.route('/menu')
def menu():
    body = { "today_special": "Mocked Special Dish" }
    status = 200
    return jsonify(body), status

@app.route('/today')
def today():
    body = { "today_special": "Signature dish is koththu for dev" }
    status = 200
    return jsonify(body), status
