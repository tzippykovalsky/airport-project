
# כנראה לא אשתמש בזה בגגל שעברתי לorm
from config.db import connect_to_db

def execute_query(query, params=None):
    try:
        with connect_to_db() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, params or ())
                if query.strip().lower().startswith("select"):
                    return cursor.fetchall()
                return None  # אם השאילתה אינה SELECT
    except Exception as e:
        return {"error": str(e)}