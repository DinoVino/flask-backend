from flask_sqlalchemy import SQLAlchemy
from models.BaseModel import *

# Have to find a way to write this more efficiently
db = SQLAlchemy(model_class=BaseModel)

class Battery(BaseModel):
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
