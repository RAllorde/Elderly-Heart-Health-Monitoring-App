import os

if __name__ == '__main__':
    os.system("pip install pysqlite3")
    os.system("pip install requests")
    os.system("pip install pyinstaller")
    os.system("pip install sklearn")
    os.system('pyinstaller --noconfirm --onefile --windowed --add-data "E:/Desktop/SCHOOL/CPE126/SERVICE LEARNING/CODE/Initialize.py;." --add-data "E:/Desktop/SCHOOL/CPE126/SERVICE LEARNING/CODE/prediction_List.py;." --add-data "E:/Desktop/SCHOOL/CPE126/SERVICE LEARNING/CODE/setup.py;." --add-data "E:/Desktop/SCHOOL/CPE126/SERVICE LEARNING/CODE/user_List.py;."  "E:/Desktop/SCHOOL/CPE126/SERVICE LEARNING/CODE/MAIN.py"')