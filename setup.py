import os

if __name__ == '__main__':
    path = os.getcwd()
    mainPATH = '"' + path + '\\MAIN.py"'
    userPATH = '"' + path + '\\user_List.py;."'
    predictionPATH = '"' + path + '\\prediction_List.py;."'
    initializePATH = '"' + path + '\\Initialize.py;."'
    imagePATH = '"' + path + '\\images;images\\"'
    iconPATH = '"' + path + '\\heart.ico"'

    mainPATH = mainPATH.replace("\\", "/")
    userPATH = userPATH.replace("\\", "/")
    predictionPATH = predictionPATH.replace("\\", "/")
    initializePATH = initializePATH.replace("\\", "/")
    imagePATH = imagePATH.replace("\\", "/")
    iconPATH = iconPATH.replace("\\", "/")

    os.system("pip install pysqlite3")
    os.system("pip install requests")
    os.system("pip install pyinstaller")
    os.system("pip install sklearn")
    os.system("pip install Pillow")
    os.system('pyinstaller --noconfirm --onedir --windowed --icon ' + iconPATH + ' --name "Elderly Heart Health Monitoring App" --add-data ' + imagePATH + ' --add-data ' + initializePATH + ' --add-data ' + predictionPATH + ' --add-data ' + userPATH + ' ' +  mainPATH)