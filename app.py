from flask import Flask
from routes.flight import flight_bp
from config.db import init_app


app = Flask(__name__)

# קריאה לפונקציה init_app כדי לאתחל את ה-SQLAlchemy עם האפליקציה
init_app(app)

# רישום הראוטים מהקובץ flight.py
app.register_blueprint(flight_bp, url_prefix="/api/flights")
# להוסיף ניתוב ליוזרס
# להוסיף ניתוב למעקב טיסות

# רק אם העמוד הזה מורץ ישירות השרת ירוץ
if __name__ == '__main__':
    app.run(port=5000)
