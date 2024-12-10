from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import MappedAsDataclass, Mapped, mapped_column, DeclarativeBase, relationship

class BaseModel(MappedAsDataclass, DeclarativeBase):
    pass
