from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate

from models import db, User, Battery

app = Flask(__name__)
# applies CORS headers to all routes, enabling resources to be accessed
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)

api = Api(app)

@app.route("/")
def helloWorld():
    return "hello world"

@app.route("/battery")
def getBatteries():
    batteries = Battery.query.all()
    return str(batteries)

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

