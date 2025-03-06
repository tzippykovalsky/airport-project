# ORM
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

load_dotenv()  # טעינת משתני הסביבה

db = SQLAlchemy()

def init_app(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = f"mssql+pyodbc://{os.getenv('DB_SERVER')}/{os.getenv('DB_NAME')}?driver=ODBC+Driver+17+for+SQL+Server"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)




# import pyodbc
# import os
# from dotenv import load_dotenv

# load_dotenv()  # טעינת משתני הסביבה

# def connect_to_db():
#     try:
#         connection = pyodbc.connect(
#             f"DRIVER={{SQL Server}};"
#             f"SERVER={os.getenv('DB_SERVER')};"
#             f"DATABASE={os.getenv('DB_NAME')};"
#         )
#         print("Connected to SQL Server")
#         return connection
#     except Exception as e:
#         print("Cannot connect to SQL Server")
#         print(e)
#         return None
