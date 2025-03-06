from config.db import db

class FlightDelay(db.Model):
    __tablename__ = 'Flight_Delays'

    delay_id = db.Column(db.Integer, primary_key=True)
    flight_id = db.Column(db.Integer, db.ForeignKey('Flights.flight_id'))
    delay_time = db.Column(db.Integer)  # זמן העיכוב בדקות
    reason = db.Column(db.String(255))

    flight = db.relationship('Flight', backref='delays')

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}