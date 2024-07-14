from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    resume = db.relationship('Resume', backref='author', uselist=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Resume(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    photo = db.Column(db.String(120))
    about = db.Column(db.Text)
    education = db.Column(db.Text)
    experience = db.Column(db.Text)
    desired_position = db.Column(db.String(120))
    additional_info = db.Column(db.Text)
    contacts = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), unique=True)
    certificates = db.relationship('Certificate', backref='resume', lazy='dynamic')

class Certificate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(120))
    uploaded_at = db.Column(db.DateTime, default=datetime.utcnow)
    resume_id = db.Column(db.Integer, db.ForeignKey('resume.id'))

@login.user_loader
def load_user(id):
    return User.query.get(int(id))