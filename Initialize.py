from asyncio.windows_events import NULL
import sqlite3
import user_List

def db_create():
    conn = sqlite3.connect('MAIN.db')
    db = conn.cursor()
    return (db, conn)

def user_TableCreate(db):
    db.execute("CREATE TABLE IF NOT EXISTS USER(Username char PRIMARY KEY, Password char)")
    return NULL

def prediction_TableCreate(db):
    db.execute("CREATE TABLE IF NOT EXISTS PREDICTION(FirstName char, LastName char, Address char, ContactNum char, Prediction char)")
    return NULL

def initialize():
    db, conn = db_create()
    user_TableCreate(db)
    prediction_TableCreate(db)
    try:
        user_List.user_Create("admin","admin123", db, conn)
    except:
        NULL