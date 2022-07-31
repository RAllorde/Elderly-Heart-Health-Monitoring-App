from asyncio.windows_events import NULL
import sqlite3
import requests
from urllib import response
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
    URL = "https://storage.googleapis.com/kagglesdsdata/datasets/1226038/2047221/heart.csv?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20220731%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20220731T022745Z&X-Goog-Expires=259199&X-Goog-SignedHeaders=host&X-Goog-Signature=72df15de4ddb23237823d1551af074727236a23032c9eedd542b1dbaa914df35aff2b47aae6c79bdaac5b27c5dbf013a4b129de0913bcc75171e6f929f5fcf97c72eb410cb6bdb5847a0e7859f3ae19158c05f2336f165fc3620693054f6244f142cd4d68e79b3a5ab86e73417a8707adb022aff1f35db472498ca43785e0dfb9023418429493566750ad29d21d600eacc4f43260839bb82d56e6c25384837167ec38edaa5bd69afdf137c1db3fc4390e01c4720bfecdeb6d0f6b748dec6cef3116ba94fe01c9c2b5ed043884759cb121c6b9eaa554bd0797a6c2d01efc5ee6b22a9fb7ff1f47b43cbf3b1b5b5137c76afada576389275201a39e6f7dea3127d"
    response = requests.get(URL)
    open("Heart Attack Anlysis.csv", "wb").write(response.content)
    db, conn = db_create()
    user_TableCreate(db)
    prediction_TableCreate(db)
    try:
        user_List.user_Create("admin","admin123", db, conn)
    except:
        NULL