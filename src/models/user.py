from src import db


class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=255))
    email = db.Column(db.String(length=255))
    password = db.Column(db.String(length=255))
    created_at = db.Column(db.DateTime())
    updated_at = db.Column(db.DateTime())

    def __init__(self, username, email, password, created_at):
        self.username = username
        self.email = email
        self.password = password
        self.created_at = created_at
