from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))




class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    users = db.relationship('User', backref='role', lazy="dynamic")

    def __repr__(self):
        return f'User {self.name}'


class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), index=True)
    email = db.Column(db.String(255), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pass_secure = db.Column(db.String(255))
  

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self, password):
        return check_password_hash(self.pass_secure, password)


class Pitch(db.Model):
        __tablename__ = 'pitch'
    
        id = db.Column(db.Integer, primary_key=True)
        pitch_title = db.Column(db.String(255))
        pitch_content = db.Column(db.String(255))
        category = db.Column(db.String(255))
        posted = db.Column(db.DateTime, default=datetime.utcnow)
        user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
        comment = db.relationship('Comment',backref = 'pitch',lazy = "dynamic")

        def save_pitch(self):
            db.session.add(self)
            db.session.commit()


        @classmethod
        def get_pitchs(cls, category):
            pitch = Pitch.query.filter_by(category=category).all()
            return pitch

        @classmethod
        def get_pitchie(cls, id):
            pitchs = Pitch.query.filter_by(id=id).first()
            return pitch


        
class Comment(db.Model):
    __tablename__ = 'comment'


    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    pitch_id = db.Column(db.Integer, db.ForeignKey("pitch.id"))


    def save_comment(self):
        db.session.add(self)
        db.session.commit()

        
 
