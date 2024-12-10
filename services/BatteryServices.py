import models.BaseModel

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

    def getBattery(batteryId):
        battery = Battery.query.filter(Battery.id == batteryId).first()
        coordinates = Coordinates.query.filter_by(batteryId=batteryId).all()

        batteryCoordinates = []
        batteryCoordinates.append(battery)
        batteryCoordinates.append(coordinates)

        return batteryCoordinates
