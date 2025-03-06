from config.db import db
from models.followed_flight import FollowedFlight
from models.user import User

class Flight(db.Model):
    __tablename__ = 'Flights'

    id = db.Column(db.Integer, primary_key=True)
    flight_number = db.Column(db.String(10), nullable=False)
    airline = db.Column(db.String(50), nullable=False)
    origin = db.Column(db.String(50), nullable=False)
    destination = db.Column(db.String(50), nullable=False)
    terminal = db.Column(db.Integer, nullable=False)
    gate = db.Column(db.String(10))
    scheduled_time = db.Column(db.DateTime, nullable=False)
    updated_time = db.Column(db.DateTime)
    status = db.Column(db.String(10), nullable=False, check_constraint="status IN ('scheduled', 'departed', 'arrived', 'delayed', 'cancelled')")

    followers = db.relationship('FollowedFlight', back_populates='flight', cascade="all, delete")

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}
