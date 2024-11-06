from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource
from flask_cors import CORS
from flask_migrate import Migrate
from models import User, Battery, Base, Coordinates
db = SQLAlchemy(model_class=Base)
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

migrate = Migrate(app,db)
db.init_app(app)
with app.app_context():
    db.create_all()

@app.route("/")
def helloWorld():
    return "hello world"

@app.route("/battery")
def getBatteries():
    return str("batteries")

#TODO: need to turn this into an API call that returns the battery with the specified ID
@app.route("/battery/<int:batteryId>")
def getBattery(batteryId):
    return f'Battery{batteryId}' 

@app.route("/user")
def getUsers():
    return "This is a list of users"

@app.route("/algorithm")
def calculateDifference():
    return str(1+1)
