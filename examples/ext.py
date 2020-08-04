from typing import TYPE_CHECKING
from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy.model import Model

db = SQLAlchemy()

if TYPE_CHECKING:
    BaseModel = db.make_declarative_base(Model)
else:
    BaseModel = db.Model
