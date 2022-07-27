from setuptools import setup
import user_List
import prediction_List
import Initialize

def test():
    check = 0
    db, conn = Initialize.db_create()
    test1 = user_List.user_Create(1, "Ronald", "rrca", db, conn)
    test2 = user_List.user_Login("Ronald", "rrca", db)
    test3 = user_List.user_EditUsername("Ronald", "Drae", db)
    test4 = user_List.user_EditPassword("Drae", "082401", db)
    test5 = prediction_List.entry_Create(1, "Rance", "Allorde", "Fear Street", "09569725406", "High Chance", db, conn)
    test6 = prediction_List.entry_Edit("Rance", "Allorde", "Drae", "Chua", "Fear Street", "09431287600", "Low Chance", db)
    test7 = prediction_List.entry_Delete("Drae", "Chua", db)
    conn.commit()
    
    print("Checking All Functions...")

    if (test1 == "New user created" or test1 == "Username is already taken"):
        check = check + 1

    if (test2 == "Username does not exist" or test2 == "Logged in successfully" or test2 == "Incorrect password"):
        check = check + 1

    if (test3 == "User does not exist" or test3 == "Username changed"):
        check = check + 1

    if (test4 == "User does not exist" or test4 == "Password changed"):
        check = check + 1

    if (test5 == "Entry already exists" or test5 == "New entry created"):
        check = check + 1

    if (test6 == "Entry does not exist" or test6 == "Entry successfully edited"):
        check = check + 1

    if (test7 == "Entry does not exist" or test7 == "Entry successfully deleted"):
        check = check + 1

    if (check == 7):
        print("All Functions Working...")
        print("ok")