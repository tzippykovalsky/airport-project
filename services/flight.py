from flask import jsonify
from models.flight import Flight

def get_all_flights():
    try:
        flights = Flight.query.all()  # מבצע שאילתה לקבלת כל הטיסות

        # הפיכת התוצאות לדיקטים
        flights_list = [flight.to_dict() for flight in flights]

        return jsonify(flights_list), 200  # מחזירים את התוצאה בפורמט JSON
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # במקרה של שגיאה


def get_flight_by_id(flight_id):
    try:
        # שימוש ב-query.get או query.filter_by כדי למצוא טיסה לפי מזהה
        flight = Flight.query.get(flight_id)

        if flight:
            return jsonify(flight.to_dict()), 200  # מחזירים את הטיסה כדיקט
        else:
            return jsonify({"error": "Flight not found"}), 404  # אם לא נמצאה טיסה עם המזהה הזה
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # במקרה של שגיאה



# from flask import jsonify
# from config.db import connect_to_db
# from utils.execute_query import execute_query

# #  בעמוד זה יש להפריד את החלק שמבצע את השאליתות עמוד נפרד
# # לראות באיזו צורה כדאי

# def get_all_flights():
#     query = 'SELECT * FROM Flights'
#     flights = execute_query(query)
#     if isinstance(flights, list):  # אם התוצאה היא רשימת משתמשים
#         flights_list = [{"id": row[0], "name": row[1], "email": row[2]} for row in flights]
#         return jsonify(flights_list)
#     return jsonify(flights), 500  # במקרה של שגיאה, מחזירים את השגיאה


# def get_flight_by_id(flight_id):
#     conn = connect_to_db()
#     if conn:
#         cursor = conn.cursor()
#         cursor.execute('SELECT * FROM Flights WHERE flight_id = ?', (flight_id,))
#         flight = cursor.fetchone()
#         conn.close()

#         if flight:
#             return jsonify({"id": flight[0], "name": flight[1], "email": flight[2]})
#         return jsonify({"error": "flight not found"}), 404
#     else:
#         return jsonify({"error": "Database connection failed"}), 500
