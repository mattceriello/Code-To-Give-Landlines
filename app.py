from flask import Flask, Blueprint, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import os
import sys

app = Flask(__name__)


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'Cod3 To Giv3'

# Connects local PostgreSQL database to Flask app
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:pwd@db/codetogive'

# Connects Heroku PostgreSQL database to Flask app
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://ikkusuespadocw:d092876418fcf499cba6f95bce285ea183e257c2c64c8f879bf91cd65a5e8c71@ec2-52-3-60-53.compute-1.amazonaws.com:5432/d27lnn9bvi72hg'


db = SQLAlchemy(app)

# Initialize Login Manager and connect to Flask app
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

with app.app_context():
    db.create_all()

# Initialize table within database to store Users and define parameters
# (Open to be changed as project progresses along)


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    firstname = db.Column(db.String(80), unique=False, nullable=False)
    lastname = db.Column(db.String(80), unique=False, nullable=False)
    password = db.Column(db.String(300), unique=False, nullable=False)

    def __init__(self, username, firstname, lastname, password):
        self.username = username
        self.firstname = firstname
        self.lastname = lastname
        self.password = password


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# Landing Route
@app.route('/')
def index():
    return render_template('index.html')

# Landing Route


@app.route('/index')
def index1():
    return render_template('index.html')


# Load Profile
@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html', username=current_user.username)

# Render Login Page


@app.route('/login')
def login():
    return render_template('login.html')


# Login Functionality
@app.route('/login', methods=['POST'])
def login_post():
    # Grab username and password from post request
    username = request.form["username"]
    password = request.form["password"]

    # Query user table
    user = User.query.filter_by(username=username).first()

    # Failed login
    if not user or not check_password_hash(user.password, password):
        flash('Login failed. Please try again')
        return redirect(url_for('login'))

    # Register login with Login Manager
    login_user(user)

    # Load profile
    return redirect(url_for('profile'))


# Render Register Page
@app.route('/register')
def register():
    return render_template('register.html')


# Register Functionality
@app.route('/register', methods=['POST'])
def register_post():
    db.create_all()
    db.session.commit()
    username = request.form['username']
    firstname = request.form['firstname']
    lastname = request.form['lastname']
    password1 = request.form['password1']
    password2 = request.form['password2']
    # check to see if username exists
    user = User.query.filter_by(username=username).first()
    if user:
        flash('Username already exists')
        return redirect(url_for('register'))

    if password1 == password2:
        print("sup")
        newUser = User(username=username, firstname=firstname, lastname=lastname,
                       password=generate_password_hash(password1, method='sha256'))
        db.session.add(newUser)
        db.session.commit()
        user = User.query.filter_by(username=username).first()
        if user is None:
            return "err: user not created"

        return redirect(url_for('login'))

    else:
        flash('Passwords don\'t match')
        return redirect(url_for('register'))


# Logout Functionality
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=port)
