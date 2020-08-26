from src import db


class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=255))
    email = db.Column(db.String(length=255))
    password = db.Column(db.String(length=255))
    date = db.Column(db.Date())

    def __init__(self, username, email, password, date):
        self.username = username
        self.email = email
        self.password = password
        self.date = date
