from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    bio = db.Column(db.String(255))
    location = db.Column(db.String(100))
    professional_status = db.Column(db.Boolean, default=False)
    role = db.Column(db.String(50), default="user")  # roles: user, manager, admin
from app import db, ma

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    name = db.Column(db.String(120))
    bio = db.Column(db.Text)
    location = db.Column(db.String(120))
    is_professional = db.Column(db.Boolean, default=False) 

    def __repr__(self):
        return '<User %r>' % self.username

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        include_fk = True
