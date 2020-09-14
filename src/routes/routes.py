import bcrypt
from flask import render_template, request, redirect, url_for, session
from src import app, db
from src.models.user import User
from datetime import date


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login', methods=['GET'])
def get_login():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def post_login():
    msg_user = ""
    user = request.form["username"]
    password = request.form["psw"]
    user_db = User.query.filter_by(username=user).first()
    if user_db is None:
        msg_user = "Username and/or password invalid"
        return render_template('login.html', msg_user=msg_user)
    else:
        if bcrypt.checkpw(password.encode('utf-8'), user_db.password.encode('utf-8')):
            session['username'] = user
            session['logged_in'] = True
            return redirect(url_for('get_profile'))
        else:
            msg_user = "Username and/or password invalid"
            return render_template('login.html', msg_user=msg_user)


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
    if count_username != 0:
        msg_user = "Username already exists!"
        return render_template('register.html', msg_user=msg_user)
    else:
        date_register = date.today()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        new_user = User(user, email, hashed_password, date_register.strftime("%Y/%m/%d"))
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('get_login'))


@app.route('/profile')
def get_profile():
    if session.get('logged_in'):
        username = session.get('username')
        return render_template('profile.html', username = username)
    else:
        return render_template('login.html')


@app.route('/edit', methods=['GET'])
def get_edit():
    if session.get('logged_in'):
        username = session.get('username')
        user = User.query.filter_by(username=username).first()
        return render_template('edit_profile.html', user=user)
    else:
        return render_template('login.html')


@app.route('/edit', methods=['POST'])
def post_edit():
    user_session = session.get('username')
    username = request.form['username']
    email = request.form['email']
    password = request.form['psw']
    password_rp = request.form['psw-repeat']
    user = User.query.filter_by(username=user_session).first()
    user.username = username
    user.email = email
    if len(password) > 0 and len(password_rp) > 0:
        if password == password_rp:
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            user.password = hashed_password
        else:
            msg_password = "Password doesn't match!"
            user = User.query.filter_by(username=username).first()
            return render_template('edit_profile.html', msg_password=msg_password, user=user)
    user.updated_at = date.today().strftime("%Y/%m/%d")
    db.session.commit()
    session['username'] = username
    return redirect(url_for('get_profile'))


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))


@app.route('/delete', methods=['POST'])
def post_delete():
    user = User.query.filter_by(username=session.get('username')).first()
    db.session.delete(user)
    db.session.commit()
    session.clear()
    return redirect(url_for('home'))