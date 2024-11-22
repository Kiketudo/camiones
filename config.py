# config.py
import pyodbc

def get_db_connection():
    conn = pyodbc.connect(
        r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
        r'DBQ=./BaseDatosBascula.accdb;'
    )
    return conn

