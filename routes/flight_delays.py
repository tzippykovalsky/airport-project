from flask import Blueprint
from services.flight_delays import get_all_flight_delays

delays_bp = Blueprint('flights_delays', __name__)

@delays_bp.route('/', methods=['GET'])
def all_flight_delays():
    return get_all_flight_delays()  