from datetime import datetime
from typing import TYPE_CHECKING

from flask import Flask

from flask_login import LoginManager, UserMixin

from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import MetaData


app = Flask(__name__)
app.config['SECRET_KEY'] = 'this-is-a-secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
login = LoginManager(app)
db = SQLAlchemy(app)

if TYPE_CHECKING:
    from flask_sqlalchemy.model import Model

    BaseModel = db.make_declarative_base(Model)
else:
    BaseModel = db.Model


class CoreMixin:
    id = db.Column(db.Integer(), primary_key=True)
    at_created = db.Column(db.DateTime(), nullable=False, default=datetime.utcnow)
    at_modified = db.Column(db.DateTime(), nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)


class Category(CoreMixin, BaseModel):
    name = db.Column(db.String(32), nullable=False, index=True, unique=True)


class User(CoreMixin, UserMixin, BaseModel):
    username = db.Column(db.String(30), nullable=False, index=True, unique=True)
    email = db.Column(db.String(255), nullable=False, index=True, unique=True)
    password = db.Column(db.String(255), nullable=False)


@login.user_loader
def load_user(id: 'str') -> 'User':
    return User.query.get(int(id))


@app.route('/')
def hello_world():
    return 'Hello, World!'


if __name__ == '__main__':
    app.run(debug=True)
