from flask import jsonify
from models.flight import Flight
from config.db import db
from datetime import datetime


# פונקציה שמחזירה את כל הטיסות לנחיתה
def get_landing_flights():
    flights = db.session.query(Flight).filter_by(destination="Ben Gurion").all()
    return jsonify([flight.to_dict() for flight in flights])


# פונקציה שמחזירה את כל הטיסות להמראה
def get_takeoff_flights():
    flights = db.session.query(Flight).filter_by(origin="Ben Gurion").all()
    return jsonify([flight.to_dict() for flight in flights])

# פונקציה לעדכון שעת ההמראה/הנחיתה
def updated_time(flight_id, new_time):
    flight = db.session.query(Flight).filter_by(id=flight_id).first()
    
    if not flight:
        return jsonify({"error": "Flight not found"}), 404

    try:
        # המרת מחרוזת לפורמט datetime אם נשלח כטקסט
        flight.updated_time = datetime.fromisoformat(new_time)  
    except ValueError:
        return jsonify({"error": "Invalid datetime format. Use ISO format (YYYY-MM-DD HH:MM:SS)"}), 400

    db.session.commit()

    return jsonify({"message": "Flight time updated successfully", "flight": flight.to_dict()})


# from sqlalchemy.orm import joinedload
# from sqlalchemy.sql import func
# from datetime import timedelta

# def get_all_flights():
#     try:
#         # שליפת כל הטיסות עם העיכובים שלהם
#         flights = db.session.query(Flight).outerjoin(FlightDelay, Flight.flight_id == FlightDelay.flight_id).all()

#         flights_list = []
#         for flight in flights:
#             flight_dict = flight.to_dict()
#             # חישוב זמן ההגעה המעודכן
#             if flight.delays and flight.delays[0].delay_time:
#                 delay_minutes = flight.delays[0].delay_time
#                 updated_arrival_time = flight.arrival_time + timedelta(minutes=delay_minutes)
#             else:
#                 updated_arrival_time = flight.arrival_time
#             flight_dict["updated_arrival_time"] = updated_arrival_time.strftime("%Y-%m-%d %H:%M:%S")
#             flights_list.append(flight_dict)

#         return jsonify(flights_list), 200
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500
