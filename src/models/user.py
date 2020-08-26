from run import db


class User:
    username = db.Column(db.String(), primary_key=True)
    email = db.Column(db.String())
    password = db.Column(db.String(length=66))
    date = db.Column(db.DATE())

    def __init__(self, username, email, password, date):
        self.username = username
        self.email = email
        self.password = password
        self.date = date
