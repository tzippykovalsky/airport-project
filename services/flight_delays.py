from flask import jsonify
from models.flight_delays import FlightDelay


def get_all_flight_delays():
    try:
        delays = FlightDelay.query.all() 

        # הפיכת התוצאות לדיקטים
        delays_list = [delay.to_dict() for delay in delays]

        return jsonify(delays_list), 200  # מחזירים את התוצאה בפורמט JSON
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # במקרה של שגיאה
