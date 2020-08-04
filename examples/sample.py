from typing import TYPE_CHECKING
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

if TYPE_CHECKING:
    from flask_sqlalchemy.model import Model

    BaseModel = db.make_declarative_base(Model)
else:
    BaseModel = db.Model


class User(BaseModel):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)


# Error: Incompatible type for "name" of "User"
# (got "int", expected "Optional[str]")
user = User(id=42, name=42)

user.id  # Inferred type is "int"
User.name  # Inferred type is "Column[Optional[str]]"
