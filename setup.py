from asyncio.windows_events import NULL
import sqlite3
import os

def db_create():
    conn = sqlite3.connect('MAIN.db')
    db = conn.cursor()
    return (db, conn)

def user_TableCreate(db):
    db.execute("CREATE TABLE IF NOT EXISTS USER(ID INT, Username char, Password char)")
    return NULL

def prediction_TableCreate(db):
    db.execute("CREATE TABLE IF NOT EXISTS PREDICTION(ID INT, FirstName char, LastName char, Address char, Prediction char)")
    return NULL

if __name__ == '__main__':
    os.system("pip install pysqlite3")
    db, conn = db_create()
    user_TableCreate(db)
    prediction_TableCreate(db)