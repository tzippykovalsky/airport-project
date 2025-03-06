from config.db import db

class Gate(db.Model):
    __tablename__ = 'Gates'

    gate_id = db.Column(db.Integer, primary_key=True)
    gate_name = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(100))
    is_open = db.Column(db.Boolean)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}
    