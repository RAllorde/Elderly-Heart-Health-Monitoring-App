from asyncio.windows_events import NULL
import sqlite3
import requests
from urllib import response

def db_create():
    conn = sqlite3.connect('MAIN.db')
    db = conn.cursor()
    return (db, conn)

def user_TableCreate(db):
    db.execute("CREATE TABLE IF NOT EXISTS USER(ID INT, Username char, Password char)")
    return NULL

def prediction_TableCreate(db):
    db.execute("CREATE TABLE IF NOT EXISTS PREDICTION(ID INT, FirstName char, LastName char, Address char, ContactNum char, Prediction char)")
    return NULL

def initialize():
    URL = "https://storage.googleapis.com/kagglesdsdata/datasets/1226038/2047221/heart.csv?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20220725%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20220725T091451Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=32394afd8d92dcab8f35a9407c03f2e62bc80d43292f89f25d49426eab867bfc860a7d1012ebfb3ffd78154cad28561f245964407645813b190e1283d0aa129d238d196f3ea1477513becea8bf4dd2fbc0a8a065215bb49c2a1e80351fdfb518abfca9557d124cfe9e0a93a1429cc90f7782398ae2a1f3ea2b9e0a4d035f200802959ca436092f53fc030d5ec9d522ba41d73a993f438c1875d53e3d6ef7b90d3f7031875483cd305aae3c7902100df4af0b6afcd7f5193b9f5455a67049efff5737021042ab5baa5e24b255db2ba3d6107251b9291c0e5c770f37cd5d2ac0cb0dde72bd60ebdf2d843580070a22e2c5f5f6145f5f0cb077d1031becc3586a0e"
    response = requests.get(URL)
    open("Heart Attack Anlysis.csv", "wb").write(response.content)
    db, conn = db_create()
    user_TableCreate(db)
    prediction_TableCreate(db)