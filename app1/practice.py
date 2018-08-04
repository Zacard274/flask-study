from flsk import Flask, requests, render_template
from flask_sqlalchemy import SQLAlchemy
from app1 import config

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)

class Users(db.Model):
    __tablename__ = 'DATA'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50))
    pwd = db.Column(db.String(50))

