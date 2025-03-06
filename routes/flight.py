from flask import Blueprint
from services.flight import get_landing_flights ,get_takeoff_flights

flight_bp = Blueprint('flights', __name__)

@flight_bp.route('/landing', methods=['GET'])
def all_landing_flights():
    return get_landing_flights()

@flight_bp.route('/takeoff', methods=['GET'])
def all_takeoff_flights():
    return get_takeoff_flights()
