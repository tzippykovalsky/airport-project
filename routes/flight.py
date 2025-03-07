from flask import Blueprint, request
from services.flight import get_landing_flights, get_takeoff_flights, updated_time

flight_bp = Blueprint('flights', __name__)

@flight_bp.route('/landing', methods=['GET'])
def all_landing_flights():
    return get_landing_flights()

@flight_bp.route('/takeoff', methods=['GET'])
def all_takeoff_flights():
    return get_takeoff_flights()

# עדכון שעת המראה/נחיתה ע"פ מזהה של טיסה
@flight_bp.route('/time/<int:flight_id>', methods=['PUT'])
def updated_time_flight(flight_id):
    return updated_time(flight_id)