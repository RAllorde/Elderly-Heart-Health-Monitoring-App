import os

if __name__ == '__main__':
    path = os.getcwd()
    mainPATH = '"' + path + '\\MAIN.py"'
    userPATH = '"' + path + '\\user_List.py;."'
    predictionPATH = '"' + path + '\\prediction_List.py;."'
    initializePATH = '"' + path + '\\Initialize.py;."'
    imagePATH1 = '"' + path + '\\assets\\button_1.png;."'
    imagePATH2 = '"' + path + '\\assets\\button_2.png;."'
    imagePATH3 = '"' + path + '\\assets\\button_3.png;."'

    mainPATH = mainPATH.replace("\\", "/")
    userPATH = userPATH.replace("\\", "/")
    predictionPATH = predictionPATH.replace("\\", "/")
    initializePATH = initializePATH.replace("\\", "/")
    imagePATH1 = imagePATH1.replace("\\", "/")
    imagePATH2 = imagePATH2.replace("\\", "/")
    imagePATH3 = imagePATH3.replace("\\", "/")

    os.system("pip install pysqlite3")
    os.system("pip install requests")
    os.system("pip install pyinstaller")
    os.system("pip install sklearn")
    os.system('pyinstaller --noconfirm --onedir --windowed --add-data ' + imagePATH1 + ' --add-data ' + imagePATH2 + ' --add-data ' + imagePATH3 + ' --add-data ' + initializePATH + ' --add-data ' + predictionPATH + ' --add-data ' + userPATH + ' ' +  mainPATH)