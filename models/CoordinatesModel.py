from flask_sqlalchemy import SQLAlchemy
from models.BaseModel import *

# Have to find a way to write this more efficiently
db = SQLAlchemy(model_class=BaseModel)

class Coordinates(BaseModel):
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
