# Graphical user interface Libraries
from tkinter import*
from tkinter import ttk
import tkinter
from typing import Literal

# Model Training Libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score



class HeartApplication:
    def __init__(self, root):
        
        #============================================FRAME DESIGN============================================#
        # Main Window
        self.root = root
        titlespace = " "
        self.root.title(125 * titlespace + "" + "Elderly Heart Health Monitoring Application")
        self.root.geometry("800x800")
        self.root.resizable(width = False, height = False)

        # Main Frame
        MainFrame = Frame(self.root, bd = 10, width = 800, height = 800, relief = RIDGE)
        MainFrame.grid()

        # Title Frame
        TitleFrame = Frame(MainFrame, bd = 7, width = 800, height = 300, relief = RIDGE)
        TitleFrame.grid(row = 0, column = 0)

        # Top Frame
        TopFrame = Frame(MainFrame, bd = 5, width = 800, height = 500, relief = RIDGE)
        TopFrame.grid(row = 1, column = 0)
        
        # Left Frame
        LeftFrameA = Frame(TopFrame, bd = 5, width = 800, height = 400, padx=2, relief = RIDGE, bg = 'powder blue')
        LeftFrameA.pack(side=LEFT)
        LeftFrameB = Frame(LeftFrameA, bd = 5, width = 800, height = 200, padx=2, pady=4, relief = RIDGE)
        LeftFrameB.pack(side=TOP, padx=0, pady=0)

        #Right Frame
        RightFrameA = Frame(TopFrame, bd = 5, width = 120, height = 800, padx=2, relief = RIDGE, bg = 'powder blue')
        RightFrameA.pack(side=RIGHT)
        RightFrameB = Frame(RightFrameA, bd = 5, width = 200, height = 250, padx=10, pady=2, relief = RIDGE)
        RightFrameB.pack(side=TOP)

        #============================================MODEL TRAININNG===========================================#

        



        
        #============================================FUNCTION DEFINITION ======================================#

        def trainModel():
            # Data Collection and Processing
            HeartAttackAPdataset = pd.read_csv('heart.csv')
            HeartAttackAPdataset.shape
            HeartAttackAPdataset.isnull().sum()

            # Splitting of Data to Training Data
            X = HeartAttackAPdataset.drop(columns='output', axis=1)
            Y = HeartAttackAPdataset['output']
            X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=2)

            # Logistic Regression
            model = LogisticRegression()
            model.fit(X_train, Y_train)

            # Accuracy Score Training Data
            X_train_prediction = model.predict(X_train)
            training_data_accuracy = accuracy_score(X_train_prediction, Y_train)

            # Accuracy Score Test Data
            X_test_prediction = model.predict(X_test)
            test_data_accuracy = accuracy_score(X_test_prediction, Y_test)

            # Get Data from Textbox
            stringAge = self.tboxAge.get()
            age = np.array(stringAge, dtype= int)

            stringSex = self.tboxSex.get()
            sex = np.array(stringSex, dtype= int)

            stringCp = self.tboxCp.get()
            cp = np.array(stringCp, dtype= int)

            stringTrtbps = self.tboxTrtbps.get()
            trtbps = np.array(stringTrtbps, dtype= int)

            stringFbs = self.tboxFbs.get()
            fbs = np.array(stringFbs, dtype= int)
            
            stringChol = self.tboxChol.get()
            chol = np.array(stringChol, dtype= int)

            stringRestecg = self.tboxRestecg.get()
            restecg = np.array(stringRestecg, dtype= int)

            stringThalachh = self.tboxThalachh.get()
            thalachh = np.array(stringThalachh, dtype= int)

            stringExng = self.tboxExng.get()
            exng = np.array(stringExng, dtype= int)

            stringOldpeak = self.tboxOldpeak.get()
            oldpeak = np.array(stringOldpeak, dtype= float)

            stringSlp = self.tboxSlp.get()
            slp = np.array(stringSlp, dtype= int)

            stringCa = self.tboxCa.get()
            ca = np.array(stringCa, dtype= int)

            stringThal = self.tboxThal.get()
            thal = np.array(stringThal, dtype= int)
            
            
            inputData = (age,sex,cp,trtbps,chol,fbs,restecg,thalachh,exng,oldpeak,slp,ca,thal)

            # Change the input data to a numpy array
            dataToArray= np.asarray(inputData)

            # Reshape the numpy array as we are predicting for only on instance
            inputDataReshaped = dataToArray.reshape(1,-1)

            prediction = model.predict(inputDataReshaped)
            print(prediction)

            if (prediction[0]== 0):
                self.lblResult = Label(RightFrameB, font=('Tahoma',12, 'bold'), text = "The Person does not \n have a Heart Disease", bd=7)
                self.lblResult.grid(row = 1, column = 0, sticky=W, padx=5)
            else:
                self.lblResult = Label(RightFrameB, font=('Tahoma',12, 'bold'), text = "The Person has \n Heart Disease", bd=7)
                self.lblResult.grid(row = 1, column = 0, sticky=W, padx=5)

        #============================================TITLE AND LABELS==========================================#
        #Title Label
        self.lbltitle = Label(TitleFrame, font=('Tahoma',20, 'bold'), text = "Elderly Heart Health Monitoring Application", bd=7)
        self.lbltitle.grid(row = 0, column = 0)

        # Age of the person
        self.lblAge = Label(LeftFrameB, font=('Tahoma',12, 'bold'), text = "Age", bd=7)
        self.lblAge.grid(row = 1, column = 0, sticky=W, padx=5)
        self.tboxAge = Entry(LeftFrameB, font=('Tahoma',12, 'bold'), bd=5, width=15, justify = 'left')
        self.tboxAge.grid(row = 1, column = 1, sticky=W, padx=5)

        # Sex of the person
        self.lblSex = Label(LeftFrameB, font=('Tahoma',12, 'bold'), text = "Sex", bd=7)
        self.lblSex.grid(row = 2, column = 0, sticky=W, padx=5)
        self.tboxSex = Entry(LeftFrameB, font=('Tahoma',12, 'bold'), bd=5, width=15, justify = 'left')
        self.tboxSex.grid(row = 2, column = 1, sticky=W, padx=5)

        # Chest Pain type chest pain type
        self.lblCp = Label(LeftFrameB, font=('Tahoma',12, 'bold'), text = "Chest Pain Type", bd=7)
        self.lblCp.grid(row = 3, column = 0, sticky=W, padx=5)
        self.tboxCp = Entry(LeftFrameB, font=('Tahoma',12, 'bold'), bd=5, width=15, justify = 'left')
        self.tboxCp.grid(row = 3, column = 1, sticky=W, padx=5)

        # Resting blood pressure (in mm Hg)
        self.lblTrtbps = Label(LeftFrameB, font=('Tahoma',12, 'bold'), text = "Resting Blood Pressure", bd=7)
        self.lblTrtbps.grid(row = 4, column = 0, sticky=W, padx=5)
        self.tboxTrtbps = Entry(LeftFrameB, font=('Tahoma',12, 'bold'), bd=5, width=15, justify = 'left')
        self.tboxTrtbps.grid(row = 4, column = 1, sticky=W, padx=5)

        # Cholestoral in mg/dl fetched via BMI sensor
        self.lblChol = Label(LeftFrameB, font=('Tahoma',12, 'bold'), text = "Cholestoral in mg/dl", bd=7)
        self.lblChol.grid(row = 5, column = 0, sticky=W, padx=5)
        self.tboxChol = Entry(LeftFrameB, font=('Tahoma',12, 'bold'), bd=5, width=15, justify = 'left')
        self.tboxChol.grid(row = 5, column = 1, sticky=W, padx=5)

        # FBS (fasting blood sugar > 120 mg/dl) (1 = true; 0 = false)
        self.lblFbs = Label(LeftFrameB, font=('Tahoma',12, 'bold'), text = "Fasting Blood Sugar", bd=7)
        self.lblFbs.grid(row = 6, column = 0, sticky=W, padx=5)
        self.tboxFbs = Entry(LeftFrameB, font=('Tahoma',12, 'bold'), bd=5, width=15, justify = 'left')
        self.tboxFbs.grid(row = 6, column = 1, sticky=W, padx=5)

        # Resting Electrocardiographic Results
        self.lblRestecg = Label(LeftFrameB, font=('Tahoma',12, 'bold'), text = "Resting Electrocardiographic Results", bd=7)
        self.lblRestecg.grid(row = 7, column = 0, sticky=W, padx=5)
        self.tboxRestecg = Entry(LeftFrameB, font=('Tahoma',12, 'bold'), bd=5, width=15, justify = 'left')
        self.tboxRestecg.grid(row = 7, column = 1, sticky=W, padx=5)

        # Maximum heart rate achieved
        self.lblThalachh = Label(LeftFrameB, font=('Tahoma',12, 'bold'), text = "Maximum Heart Rate", bd=7)
        self.lblThalachh.grid(row = 8, column = 0, sticky=W, padx=5)
        self.tboxThalachh = Entry(LeftFrameB, font=('Tahoma',12, 'bold'), bd=5, width=15, justify = 'left')
        self.tboxThalachh.grid(row = 8, column = 1, sticky=W, padx=5)

        # Exercise induced angina (1 = yes; 0 = no)
        self.lblExng = Label(LeftFrameB, font=('Tahoma',12, 'bold'), text = "Exercise Induced Angina", bd=7)
        self.lblExng.grid(row = 9, column = 0, sticky=W, padx=5)
        self.tboxExng = Entry(LeftFrameB, font=('Tahoma',12, 'bold'), bd=5, width=15, justify = 'left')
        self.tboxExng.grid(row = 9, column = 1, sticky=W, padx=5)

        # Previous Peak
        self.lblOldpeak = Label(LeftFrameB, font=('Tahoma',12, 'bold'), text = "Previous Peak", bd=7)
        self.lblOldpeak.grid(row = 10, column = 0, sticky=W, padx=5)
        self.tboxOldpeak = Entry(LeftFrameB, font=('Tahoma',12, 'bold'), bd=5, width=15, justify = 'left')
        self.tboxOldpeak.grid(row = 10, column = 1, sticky=W, padx=5)

        # Slope
        self.lblSlp = Label(LeftFrameB, font=('Tahoma',12, 'bold'), text = "Slope", bd=7)
        self.lblSlp.grid(row = 11, column = 0, sticky=W, padx=5)
        self.tboxSlp = Entry(LeftFrameB, font=('Tahoma',12, 'bold'), bd=5, width=15, justify = 'left')
        self.tboxSlp.grid(row = 11, column = 1, sticky=W, padx=5)

        # Number of Major Vessels
        self.lblCa = Label(LeftFrameB, font=('Tahoma',12, 'bold'), text = "Number of Major Vessels", bd=7)
        self.lblCa.grid(row = 12, column = 0, sticky=W, padx=5)
        self.tboxCa = Entry(LeftFrameB, font=('Tahoma',12, 'bold'), bd=5, width=15, justify = 'left')
        self.tboxCa.grid(row = 12, column = 1, sticky=W, padx=5)

        # Thal Rate
        self.lblThal = Label(LeftFrameB, font=('Tahoma',12, 'bold'), text = "Thal Rate", bd=7)
        self.lblThal.grid(row = 13, column = 0, sticky=W, padx=5)
        self.tboxThal = Entry(LeftFrameB, font=('Tahoma',12, 'bold'), bd=5, width=15, justify = 'left')
        self.tboxThal.grid(row = 13, column = 1, sticky=W, padx=5)


    
        # Status
        self.lblStatus = Label(RightFrameB, font=('Tahoma',12, 'bold'), text = "Status:", bd=7)
        self.lblStatus.grid(row = 0, column = 0, sticky=W, padx=5)
        self.lblResult = Label(RightFrameB, font=('Tahoma',12, 'bold'), text = "No Analysis", bd=7)
        self.lblResult.grid(row = 1, column = 0, sticky=W, padx=5)

        #============================================BUTTONS===================================================#
        # Predict
        self.btnPredict = Button(RightFrameB, font=('tahoma',16,'bold'), text = "Predict", bd=4, pady=1, padx=24, width=6, height=2, command = trainModel).grid(row=2, column=0, padx=1)
      
if __name__=='__main__':
    #Creating Window
    root = Tk() 
    application = HeartApplication(root)
    root.mainloop()