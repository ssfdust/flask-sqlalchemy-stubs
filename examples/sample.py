from typing import TYPE_CHECKING, TypeVar, Type
from flask_sqlalchemy import SQLAlchemy, BaseQuery
from flask_sqlalchemy.model import Model


M = TypeVar("M", bound="CompletionModel")


class CompletionModel(Model):
    @classmethod
    def cquery(cls: Type[M]) -> BaseQuery[M]:
        return cls.query


db = SQLAlchemy(model_class=CompletionModel)

if TYPE_CHECKING:
    BaseModel = db.make_declarative_base(CompletionModel)
else:
    BaseModel = db.Model


class User(BaseModel):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)


# Error: Incompatible type for "name" of "User"
# (got "int", expected "Optional[str]")
user = User(id=42, name=42)
u = User.query.filter_by(name=1).one()

user.id  # Inferred type is "int"
User.name  # Inferred type is "Column[Optional[str]]"

u = User.query.filter_by(name=1).one()  # Inferred type is 'sample.User*'
u.id  # Inferred type is "int"
