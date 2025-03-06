from config.db import db

class FollowedFlight(db.Model):
    __tablename__ = 'Followed_Flights'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('Users.id', ondelete="CASCADE"), nullable=False)
    flight_id = db.Column(db.Integer, db.ForeignKey('Flights.id', ondelete="CASCADE"), nullable=False)

    user = db.relationship('User', back_populates='followed_flights')
    flight = db.relationship('Flight', back_populates='followers')

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}
    