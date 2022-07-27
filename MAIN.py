import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import user_List
import Initialize

db, conn = Initialize.db_create()
  
 
LARGEFONT =("Verdana", 35)
  
class tkinterApp(tk.Tk):
     
    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
         
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
         
        # creating a container
        container = tk.Frame(self) 
        container.pack(side = "top", fill = "both", expand = True)
  
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
  
        # initializing frames to an empty array
        self.frames = {} 
        self.title("Elderly Heart Health Monitoring Application")

        # iterating through a tuple consisting
        # of the different page layouts
        for F in (StartPage, Page1, Page2):
  
            frame = F(container, self)
  
            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame
  
            frame.grid(row = 0, column = 0, sticky ="nsew")
  
        self.show_frame(StartPage)
  
    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
  
# first window frame startpage
  
class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # Title Frame
        TitleFrame = Frame(self, bd = 7, width = 500, height = 300, relief = RIDGE)
        TitleFrame.grid(row = 0, column = 0)

        # Top Frame
        TopFrame = Frame(self, bd = 5, width = 800, height = 500, relief = RIDGE)
        TopFrame.grid(row = 1, column = 0)

        ButtonFrame = Frame(self, bd = 5, width = 800, height = 500, relief = RIDGE)
        ButtonFrame.grid(row = 2, column = 0)

        #============================================TITLE AND LABELS==========================================#
        #Title Label
        self.lbltitle = Label(TitleFrame, font=('Tahoma',12, 'bold'), text = "Welcome to \n Elderly Heart Health Monitoring \n Application", bd=7)
        self.lbltitle.grid(row = 0, column = 0)

        # Username
        self.lblUsername = Label(TopFrame, font=('Tahoma',12, 'bold'), text = "Username: ", bd=7)
        self.lblUsername.grid(row = 1, column = 0, sticky=W, padx=5)
        self.tboxUsername = Entry(TopFrame, font=('Tahoma',12, 'bold'), bd=5, width=15, justify = 'left')
        self.tboxUsername.grid(row = 1, column = 1, sticky=W, padx=5)

        # Password
        self.lblPassword = Label(TopFrame, font=('Tahoma',12, 'bold'), text = "Password: ", bd=7)
        self.lblPassword.grid(row = 2, column = 0, sticky=W, padx=5)
        self.tboxPassword = Entry(TopFrame, font=('Tahoma',12, 'bold'), bd=5, width=15, justify = 'left')
        self.tboxPassword.grid(row = 2, column = 1, sticky=W, padx=5)
        
        def Login():
            Username = self.tboxUsername.get()
            Password = self.tboxPassword.get()

            response = user_List.user_Login(Username, Password, db)

            if (response == "Username does not exist"):
                messagebox.showinfo("Login Error", "Username does not exist")

            elif (response == "Logged in successfully"):
                controller.show_frame(Page1)

            else:
                messagebox.showinfo("Login Error", "Incorrect password")


        #============================================BUTTONS===================================================#
        # Predict
        self.btnPredict = Button(ButtonFrame, font=('tahoma',16,'bold'), text = "Login", bd=4, pady=1, padx=24, width=5, height=1, command = Login).grid(row=0, column=0, padx=1)
 
        # button1 = ttk.Button(self, text ="Page 1",
        # command = lambda : controller.show_frame(Page1))
     
        # # putting the button in its place by
        # # using grid
        # button1.grid(row = 1, column = 1, padx = 10, pady = 10)
  
        # ## button to show frame 2 with text layout2
        # button2 = ttk.Button(self, text ="Page 2",
        # command = lambda : controller.show_frame(Page2))
     
        # # putting the button in its place by
        # # using grid
        # button2.grid(row = 2, column = 1, padx = 10, pady = 10)
  
          
  
  
# second window frame page1
class Page1(tk.Frame):
     
    def __init__(self, parent, controller):
         
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Page 1", font = LARGEFONT)
        label.grid(row = 0, column = 4, padx = 10, pady = 10)
  
        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text ="StartPage",
                            command = lambda : controller.show_frame(StartPage))
     
        # putting the button in its place
        # by using grid
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)
  
        # button to show frame 2 with text
        # layout2
        button2 = ttk.Button(self, text ="Page 2",
                            command = lambda : controller.show_frame(Page2))
     
        # putting the button in its place by
        # using grid
        button2.grid(row = 2, column = 1, padx = 10, pady = 10)
  
  
  
  
# third window frame page2
class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Page 2", font = LARGEFONT)
        label.grid(row = 0, column = 4, padx = 10, pady = 10)
  
        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text ="Page 1",
                            command = lambda : controller.show_frame(Page1))
     
        # putting the button in its place by
        # using grid
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)
  
        # button to show frame 3 with text
        # layout3
        button2 = ttk.Button(self, text ="Startpage",
                            command = lambda : controller.show_frame(StartPage))
     
        # putting the button in its place by
        # using grid
        button2.grid(row = 2, column = 1, padx = 10, pady = 10)
  
  
# Driver Code
if __name__ == '__main__':
    Initialize.initialize()
    app = tkinterApp()
    app.mainloop()