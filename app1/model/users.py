from file1.model.base import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50))
    pwd = db.Column(db.Integer)

    def __init__(self, name, pwd):
        self.name = name
        self.pwd = pwd

