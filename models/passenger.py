from config.db import db

class Passenger(db.Model):
    __tablename__ = 'Passengers'

    passenger_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    passport_number = db.Column(db.String(50))
    flight_id = db.Column(db.Integer, db.ForeignKey('Flights.flight_id'))

    flight = db.relationship('Flight', backref='passengers')

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}
    