from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, relationship

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True) 
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email
        }
    
class Battery(db.Model):
    __tablename__ = 'batteries'
    id: Mapped[int] = mapped_column(primary_key=True)
    status = db.Column(db.String(25), unique=True, nullable=False)
    type = db.Column(db.String(50), unique=True, nullable=False)
    coordinates: Mapped[list["Coordinates"]] = relationship(back_populates = "battery")

    def to_dict(self):
        return{
            'id': self.id,
            'status': self.status
        }

# TODO: We should add a category for the type of damage it has suffered.
# This will help refine the model and aid the enduser.
# In the application layer, we need to implement the code that assigns an enum/string.  
class Coordinates(db.Model):
    __tablename__ = 'coordinates'
    id: Mapped[int] = mapped_column(primary_key=True)
    batteryId: Mapped[int] = mapped_column(ForeignKey("batteries.id"))
    battery: Mapped["Battery"] = relationship(back_populates="coordinates")

def initDB():
    db.create_all()

if __name__ == "__main__":
    initDB()
