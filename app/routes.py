from flask import json, jsonify
from app import app
from app import db
from app.models import Menu

@app.route('/')
def home():
	return jsonify({ 
        "message": "Welcome to our amazing restaurant!",
        "greeting": "Thank you for visiting us today",
        "service": "We're here to serve you the best food"
    }), 200

@app.route('/menu')
def menu():
    today = Menu.query.first() 
    if today:
        body = { "today_special": today.name }
        status = 200
    else:
        body = { "error": "Sorry, the service is not available today." }
        status = 404
    return jsonify(body), status

@app.route('/dish')
def dish():
    featured = Menu.query.offset(1).first() 
    if featured:
        body = { "featured_dish": featured.name }
        status = 200
    else:
        body = { "error": "No featured dish available today." }
        status = 404
    return jsonify(body), status