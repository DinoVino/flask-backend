from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource
from flask_cors import CORS
from flask_migrate import Migrate
from sqlalchemy import MetaData
from models.BaseModel import *
import json

# This part is all about instantiating the database, should be moved to a separate class instead to make it clean.
# Should just be part of a service.
db = SQLAlchemy(model_class=BaseModel)
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
migrate = Migrate(app,db)
db.init_app(app)
migrate.init_app(app,db, render_as_batch=True)
with app.app_context():
    db.create_all()

@app.route("/")
def helloWorld():
    return "hello world"

@app.route("/battery")
def getBatteries():
    # batteries = db.session.execute(db.select(Battery).order_by(Battery.id)).scalars()
    return str("hello")

#TODO: need to turn this into an API call that returns the battery with the specified ID
@app.route("/battery/<int:id>")
def getBattery(id):
    battery = db.get_or_404(Battery, id)
    return "Battery Status: " + battery.status + ", Battery Type: " + battery.type

@app.route("/user/<int:id>")
def getUser(id):
    user = db.get_or_404(User, id)
    return user.username

@app.route("/coordinates")
def getCoordinates():
    coordinates = db.session.execute(db.select(Coordinates).order_by(Coordinates.id)).scalars()
    return coordinates

@app.route("/algorithm")
def calculateDifference():
    return str(1+1)

@app.route("/testGenerate")
def createBatteryWithCoordinates():
    # coordinates = Coordinates(x=3, y=5, batteryId=1)
    # cood = []
    # cood.append(coordinates)
    # battery = Battery(id=None, status="Broken", type="Tesla", coordinates=cood)
    # db.session.add(coordinates)
    # db.session.add(battery)
    # coordinates.verified = True
    # battery.verified = True
    # db.session.commit()
    battery = db.get_or_404(Battery, 1)
    return battery.coordinates
