from flask import Flask
from ext import db
from models import User

app = Flask(__name__)
db.init_app(app)


def index() -> str:
    user = User.query.get_or_404(1)
    return user.name or ""


app.add_url_rule("/", "index", index)
