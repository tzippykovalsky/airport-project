from flask import Blueprint
from services.flight import get_all_flights, get_flight_by_id

flight_bp = Blueprint('flights', __name__)

@flight_bp.route('/', methods=['GET'])
def all_flights():
    return get_all_flights()  

@flight_bp.route('/<int:flight_id>', methods=['GET'])
def flight_by_id(flight_id):
    return get_flight_by_id(flight_id)  
