from datetime import datetime
from typing import Optional
from .. import app_factory
from flask_bcrypt import Bcrypt
 
db = app_factory.main_controller.db
 

# Define the UserInfoEntry model
class UserInfo(db.Model):
    user_id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username: str = db.Column(db.String(100), nullable=False)
    hashed_password: str = db.Column(db.String(200), nullable=False)
    email: str = db.Column(db.String(100), nullable=False)
    phone_number: str = db.Column(db.String(8), nullable=True)
    points: str = db.Column(db.Integer, nullable=True)
    created_on = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    
    def to_dict(self):
        return {
            "user_id": self.user_id,
            "username": self.username,
            "hashed_password": self.hashed_password,
            "email": self.email,
            "phone_number": self.phone_number,
            "points": self.points,
            "created_on": self.created_on
        }
 
    def __repr__(self) -> str:
        return f"<UserInfo(user_id={self.user_id}, username={self.username}, hashed_password={self.hashed_password}, email={self.email}, created_on={self.created_on}, phone_number={self.phone_number}, points={self.points})>"
    

    @staticmethod
    def hash_password(password):
        # Hash password
        bcrypt = Bcrypt()
        return bcrypt.generate_password_hash(password).decode('utf-8')

    @staticmethod
    def check_password(hashed_password, password):
        # Check Hash password VS password
        bcrypt = Bcrypt()
        return bcrypt.check_password_hash(hashed_password, password)

