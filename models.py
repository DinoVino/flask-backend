from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import MappedAsDataclass, Mapped, mapped_column, DeclarativeBase, relationship

class Base(MappedAsDataclass, DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    username:Mapped[str] = mapped_column(unique=True, nullable=False)
    email:Mapped[str]

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email
        }

class Battery(Base):
    __tablename__ = 'batteries'
    id: Mapped[int] = mapped_column(primary_key=True)
    status: Mapped[str] = mapped_column(unique=True, nullable=False)
    type: Mapped[str] = mapped_column(unique=True, nullable=False)
    coordinates: Mapped[list["Coordinates"]] = relationship(back_populates = "battery")

    def to_dict(self):
        return{
            'id': self.id,
            'status': self.status
        }

class Coordinates(Base):
    __tablename__ = 'coordinates'
    id: Mapped[int] = mapped_column(primary_key=True)
    x: Mapped[int] = mapped_column(nullable=False)
    y: Mapped[int] = mapped_column(nullable=False)
    battery_id: Mapped[int] = mapped_column(ForeignKey("batteries.id"))
    battery: Mapped["Battery"] = relationship(back_populates="coordinates")
    comment: Mapped[str] = mapped_column(nullable=True, server_default="Should add a comment")

    def __init__(self, x, y, batteryId, comment):
        self.x = x
        self.y = y
        self.batteryId = batteryId
        self.comment = comment

    def to_dict(self):
        return{
            'id': self.id,
            'x': self.x,
            'y' : self.y,
            'battery_id': self.battery_id,
            'comment': self.comment
        }
