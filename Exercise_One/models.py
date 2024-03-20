from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from Crypto.Cipher import AES
from datetime import datetime

db = SQLAlchemy()
bcrypt = Bcrypt()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)

class RevokedTokenModel(db.Model):
    jti = db.Column(db.String(120), primary_key=True)
    blacklisted_on = db.Column(db.DateTime, nullable=False, default=datetime.now)

    def add(self):
        db.session.add(self)
        db.session.commit()

class Calendar(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    name = db.Column(db.String(128), nullable=False)
    description = db.Column(db.Text, nullable=True)
    data = db.Column(db.LargeBinary, nullable=False)
    key = db.Column(db.LargeBinary, nullable=False)  # Add a column to store the encryption key

    def __init__(self, user_id, name, description, data, key):
        self.user_id = user_id
        self.name = name
        self.description = description
        self.data = self.encrypt(data, key)
        self.key = key  # Store the encryption key

    def encrypt(self, data, key):
        cipher = AES.new(key, AES.MODE_EAX)
        ciphertext, tag = cipher.encrypt_and_digest(data)
        return cipher.nonce + tag + ciphertext

class Alert(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    calendar_id = db.Column(db.Integer, db.ForeignKey('calendar.id', ondelete='CASCADE'), nullable=False)
    title = db.Column(db.String(128), nullable=False)
    description = db.Column(db.Text, nullable=True)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)