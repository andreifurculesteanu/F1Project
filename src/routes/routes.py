from flask import render_template, request, redirect, url_for
from src import app, db
from src.models.user import User
from datetime import date


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/register', methods=['GET'])
def get_register():
    return render_template('register.html')


@app.route('/register', methods=['POST'])
def post_register():
    msg_password = ""
    msg_user = ""
    user = request.form["username"]
    email = request.form["email"]
    password = request.form["psw"]
    password_repeat = request.form["psw-repeat"]
    if password != password_repeat:
        msg_password = "Password doesn't match!"
        return render_template('register.html', msg_password=msg_password)
    count_username = User.query.filter_by(username=user).count()
    print(count_username)
    if count_username != 0:
        msg_user = "Username already exists!"
        return render_template('register.html', msg_password=msg_password)
    else:
        date_register = date.today()
        new_user = User(user, email, password, date_register.strftime("%Y/%m/%d"))
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))