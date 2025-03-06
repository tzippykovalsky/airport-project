from flask import jsonify
from models.flight import Flight
from config.db import db

# פונקציה שמחזירה את כל הטיסות לנחיתה
def get_landing_flights():
    flights = db.session.query(Flight).filter_by(destination="Ben Gurion").all()
    return jsonify([flight.to_dict() for flight in flights])


# פונקציה שמחזירה את כל הטיסות להמראה
def get_takeoff_flights():
    flights = db.session.query(Flight).filter_by(origin="Ben Gurion").all()
    return jsonify([flight.to_dict() for flight in flights])


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


# def get_flight_by_id(flight_id):
#     try:
#         # שימוש ב-query.get או query.filter_by כדי למצוא טיסה לפי מזהה
#         flight = Flight.query.get(flight_id)

#         if flight:
#             return jsonify(flight.to_dict()), 200  # מחזירים את הטיסה כדיקט
#         else:
#             return jsonify({"error": "Flight not found"}), 404  # אם לא נמצאה טיסה עם המזהה הזה
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500  # במקרה של שגיאה

