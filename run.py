from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/register')
def register():
    return render_template('register.html')


db = SQLAlchemy(app)
migrate = Migrate(app, db)

if __name__ == '__main__':
    app.config.from_pyfile('./config/config.cfg')
    app.run()

