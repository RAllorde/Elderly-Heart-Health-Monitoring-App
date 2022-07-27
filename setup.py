import os

if __name__ == '__main__':
    os.system("pip install pysqlite3")
    os.system("pip install requests")
    os.system("pip install pyinstaller")
    os.system("pip install sklearn")
    os.system("pyinstaller -F --onefile --add-data user_List.py;MAIN.py --add-data prediction_List.py;MAIN.py --add-data TEST.py;MAIN.py MAIN.py")