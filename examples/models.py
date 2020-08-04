from ext import BaseModel, db


class User(BaseModel):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    address = db.relationship(
        "Address", uselist=True, primaryjoin="foreign(Address.uid) == User.id"
    )


class Address(BaseModel):

    __tablename__ = "address"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    uid = db.Column(db.Integer)
