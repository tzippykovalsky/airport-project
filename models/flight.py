from config.db import db
from models.gate import Gate

class Flight(db.Model):
    __tablename__ = 'Flights'

    flight_id = db.Column(db.Integer, primary_key=True)
    flight_number = db.Column(db.String(50), nullable=False)
    departure_airport = db.Column(db.String(100))
    arrival_airport = db.Column(db.String(100))
    departure_time = db.Column(db.DateTime)
    arrival_time = db.Column(db.DateTime)
    status = db.Column(db.String(50))
    gate_id = db.Column(db.Integer, db.ForeignKey('Gates.gate_id'))

    gate = db.relationship('Gate', backref='flights')

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}
    