from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, relationship

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True) 
    username:Mapped[str] = mapped_column(unique=True, nullable=False)
    email:Mapped[str] = mapped_column(unique=True, nullable=False)

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

# TODO: We should add a category for the type of damage it has suffered.
# This will help refine the model and aid the enduser.
# In the application layer, we need to implement the code that assigns an enum/string.  
class Coordinates(Base):
    __tablename__ = 'coordinates'
    id: Mapped[int] = mapped_column(primary_key=True)
    batteryId: Mapped[int] = mapped_column(ForeignKey("batteries.id"))
    battery: Mapped["Battery"] = relationship(back_populates="coordinates")
