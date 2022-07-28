from asyncio.windows_events import NULL
from types import NoneType

def user_Create(username, password, db, conn):
    db.execute("SELECT Username FROM USER WHERE Username=:Username", 
        {'Username': username})
    conn.commit()

    if (type(db.fetchone()) == NoneType):
        log_Message = "New user created"
        db.execute("INSERT INTO USER(Username, Password) VALUES (:Username, :Password)", 
            {'Username': username, "Password": password})
        conn.commit()
    
    else:
        log_Message = "Username is already taken"

    return log_Message

def user_Login(username, password, db):
    db.execute("SELECT Username FROM USER WHERE Username=:Username", 
        {'Username': username})
    
    if (type(db.fetchone()) == NoneType):
        log_Message = "Username does not exist"

    else:
        db.execute("SELECT * FROM USER WHERE Username=:Username", 
        {'Username': username})
        if (db.fetchone()[1] == password):
            log_Message = "Logged in successfully"
        else:
            log_Message = "Incorrect password"

    return log_Message

def user_CheckDatabase(db):
    db.execute("SELECT * FROM USER")
    user_List = db.fetchall()
    return user_List

def user_EditUsername(username_old, username_new, db):
    db.execute("SELECT Username FROM USER WHERE Username=:Username", 
        {'Username': username_old})
    
    if (type(db.fetchone()) == NoneType):
        log_Message = "User does not exist"
    
    else:
        db.execute("UPDATE USER set Username=:Username_new WHERE Username=:Username_old", 
            {'Username_new': username_new, 'Username_old': username_old})

        log_Message = "Username changed"
    return log_Message

def user_EditPassword(username, password_new, db):
    db.execute("SELECT Username FROM USER WHERE Username=:Username", 
        {'Username': username})
    
    if (type(db.fetchone()) == NoneType):
        log_Message = "User does not exist"

    else:
        db.execute("UPDATE USER set Password=:Password_new WHERE Username=:Username", 
            {'Password_new': password_new, 'Username': username})
            
        log_Message = "Password changed"
    return log_Message