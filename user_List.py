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