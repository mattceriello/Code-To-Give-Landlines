from flask import Flask, Blueprint, render_template, redirect, url_for, request, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask_cors import CORS
import os
import sys

app = Flask(__name__)


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'Cod3 To Giv3'
CORS(app)

# Connects local PostgreSQL database to Flask app
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:pwd@db/codetogive'

# Connects Heroku PostgreSQL database to Flask app
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://tdlixfnucgirtt:f4b8e06465c23212247ad430912af82eac34db6988e6bc263ce046fa03cd466d@ec2-52-21-136-176.compute-1.amazonaws.com:5432/d3c01e59q00k31'


db = SQLAlchemy(app)

# Initialize Login Manager and connect to Flask app
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

# with app.app_context():
# db.create_all()

# Initialize table within database to store Users and define parameters
# (Open to be changed as project progresses along)


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    firstname = db.Column(db.String(80), unique=False, nullable=False)
    lastname = db.Column(db.String(80), unique=False, nullable=False)
    password = db.Column(db.String(300), unique=False, nullable=False)
    email = db.Column(db.String(80), unique=False, nullable=False)
    phone = db.Column(db.String(15), unique=False, nullable=False)
    age = db.Column(db.Integer, unique=False, nullable=False)

    def __init__(self, username=None, firstname=None, lastname=None, password=None, email=None, phone=None, age=None):
        self.username = username
        self.firstname = firstname
        self.lastname = lastname
        self.password = password
        self.email = email
        self.phone = phone
        self.age = age

    def serialize(self):
        return {"id": self.id,
                "username": self.username,
                "firstname": self.firstname,
                "lastname": self.lastname,
                "password": self.password,
                "email": self.email,
                "phone": self.phone,
                "age": self.age}


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


with app.app_context():
    db.create_all()
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


# Login Functionality
@app.route('/login', methods=['POST'])
def login():
    # Grab username and password from post request
    username = request.json["username"]
    password = request.json["password"]

    # Query user table
    user = User.query.filter_by(username=username).first()

    # Failed login
    if not user or not check_password_hash(user.password, password):
        return jsonify('Login failed. Please try again'), 404
    # Load profile
    return jsonify({"user": user.serialize()}), 200


# Register Functionality
@app.route('/register', methods=['POST'])
def register_user():
    db.create_all()
    db.session.commit()
    username = request.json['username']
    firstname = request.json['firstname']
    lastname = request.json['lastname']
    password1 = request.json['password1']
    password2 = request.json['password2']
    email = request.json['email']
    phone = request.json['phone']
    age = request.json['age']
    # check to see if username exists
    user = User.query.filter_by(username=username).first()
    if user:
        return jsonify({"error": 'Username already exists'}), 400

    if password1 == password2:
        print("sup")
        newUser = User(username=username, firstname=firstname, lastname=lastname, password=generate_password_hash(
            password1, method='sha256'), email=email, phone=phone, age=age)
        db.session.add(newUser)
        db.session.commit()
        user = User.query.filter_by(username=username).first()
        if user is None:
            return jsonify({"err: user not created"}), 400

        return jsonify({"user": newUser.serialize()}), 200

    else:
        return jsonify({'Passwords don\'t match'}), 400


# Logout Functionality
@ app.route('/logout')
@ login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=port, debug=True)
