from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource
from flask_cors import CORS
from flask_migrate import Migrate
from models import User, Battery, Coordinates, Base
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
    batteries = db.session.execute(db.select(Battery).order_by(Battery.id)).scalars()
    return str(batteries.first())

#TODO: need to turn this into an API call that returns the battery with the specified ID
@app.route("/battery/<int:id>")
def getBattery(id):
    battery = db.get_or_404(Battery, id)
    return battery.status

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
