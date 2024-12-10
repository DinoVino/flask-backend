from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import MappedAsDataclass, Mapped, mapped_column, DeclarativeBase, relationship
from models.BaseModel import *

class User(BaseModel):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True)
    username:Mapped[str] = mapped_column(unique=True, nullable=False)
    email:Mapped[str]

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email
        }
