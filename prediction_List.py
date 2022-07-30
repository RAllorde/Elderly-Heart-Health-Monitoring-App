from asyncio.windows_events import NULL
from types import NoneType

def entry_Create(first_Name, last_Name, address, contact_Num, prediction, db, conn):
    db.execute("SELECT FirstName FROM PREDICTION WHERE FirstName=:first_Name AND LastName=:last_Name", 
        {'first_Name': first_Name, 'last_Name': last_Name})
    conn.commit()

    if (type(db.fetchone()) == NoneType):
        log_Message = "New entry created"
        db.execute("INSERT INTO PREDICTION(FirstName, LastName, Address, ContactNum, Prediction) VALUES (:first_Name, :last_Name, :address, :prediction, :contact_Num)", 
            {'first_Name': first_Name, "last_Name": last_Name, "address": address, "prediction": prediction, "contact_Num": contact_Num})
        conn.commit()
    
    else:
        log_Message = "Entry already exists"

    return log_Message

def entry_Delete(first_Name, last_Name, db, conn):
    db.execute("SELECT FirstName FROM PREDICTION WHERE FirstName=:first_Name AND LastName=:last_Name", 
        {'first_Name': first_Name, 'last_Name': last_Name})
    
    if (type(db.fetchone()) == NoneType):
        log_Message = "Entry does not exist"

    else:
        db.execute("DELETE FROM PREDICTION WHERE FirstName=:first_Name AND LastName=:last_Name", 
        {'first_Name': first_Name, 'last_Name': last_Name})
        log_Message = "Entry successfully deleted"
    conn.commit()
    return log_Message

def entry_CheckList(db):
    db.execute("SELECT * FROM PREDICTION")
    prediction_List = db.fetchall()
    return prediction_List

def entry_Edit(first_Name_Old, last_Name_Old, first_Name, last_Name, contact_Num, address, prediction, db, conn):
    db.execute("SELECT FirstName FROM PREDICTION WHERE FirstName=:first_Name_Old AND LastName=:last_Name_Old", 
        {'first_Name_Old': first_Name_Old, 'last_Name_Old': last_Name_Old})
    
    if (type(db.fetchone()) == NoneType):
        log_Message = "Entry does not exist"
    
    else:
        db.execute("UPDATE PREDICTION set FirstName=:first_Name, LastName=:last_Name, Address=:address, Prediction=:prediction, ContactNum=:contact_Num WHERE FirstName=:first_Name_Old AND LastName=:last_Name_Old", 
            {'first_Name': first_Name, "last_Name": last_Name, "address": address, "prediction": prediction, "contact_Num": contact_Num, "first_Name_Old": first_Name_Old, "last_Name_Old": last_Name_Old})

        log_Message = "Entry successfully edited"

    conn.commit()
    return log_Message