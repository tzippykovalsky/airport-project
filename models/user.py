from config.db import db

class User(db.Model):
    __tablename__ = 'Users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(10), nullable=False, check_constraint="role IN ('user', 'admin')")

    followed_flights = db.relationship('FollowedFlight', back_populates='user', cascade="all, delete")

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}
