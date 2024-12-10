from models import *

class BatteryServices:
    def __init__(self, db):
        self.db = db

    def getBatteries():
        batteries = Battery.query.all()
        cooridnates = Coordinates.query.all()

        batteriesCoordinatesContainer = []
        batteriesCoordinatesContainer.append(batteries)
        batteriesCoordinatesContainer.append(coordinates)

        return batteriesCoordinatesContainer
