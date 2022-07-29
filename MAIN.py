from cgitb import text
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from turtle import bgcolor
from venv import create
import user_List
import Initialize
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

db, conn = Initialize.db_create()
LARGEFONT =("Verdana", 70)
  
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
        for F in (LoginPage, MainMenu, Signup, Page2):
  
            frame = F(container, self)
  
            # initializing frame of that object from
            # LoginPage, MainMenu, page2 respectively with
            # for loop
            self.frames[F] = frame
  
            frame.grid(row = 0, column = 0, sticky ="nsew")
            frame.grid_remove()

        self.show_frame(LoginPage)
  
    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
        frame.grid()
  
# first window frame LoginPage

#============================================================================================================================================================================================================#  
class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # Title Frame
        TitleFrame = Frame(self, bd = 7, width = 500, height = 300, bg = "#047857")
        TitleFrame.grid(row = 0, column = 0)

        # Top Frame
        TopFrame = Frame(self, bd = 0, width = 800, height = 500, relief = RIDGE)
        TopFrame.grid(row = 1, column = 0)

        ButtonFrame = Frame(self, bd = 0, width = 800, height = 500, padx=1, pady=1)
        ButtonFrame.grid(row = 2, column = 0, padx=15, pady=15)

        #============================================TITLE AND LABELS==========================================#
        def temp_text_username(e):
            self.tboxUsername.delete(0,"end")
            self.tboxUsername.configure(fg="Black")

        def temp_text_password(e):
            self.tboxPassword.delete(0,"end")
            self.tboxPassword.configure(fg="Black")
        
        #Title Label
        self.lbltitle = Label(TitleFrame, font=('Tahoma',14, 'bold'), text = "Welcome to the \n Elderly Heart Health \n Monitoring App", bd=10, fg="white", bg="#047857")
        self.lbltitle.grid(row = 0, column = 0, padx=40)

        # Username
        self.tboxUsername = Entry(TopFrame, font=('Tahoma',12, 'bold'), bd=1, width=20, justify = 'left',fg="Gray70")
        self.tboxUsername.insert(0, "Username...")
        self.tboxUsername.bind("<FocusIn>", temp_text_username)
        self.tboxUsername.grid(row = 1, column = 0, sticky=W, padx=5, pady=10)

        # Password
        self.tboxPassword = Entry(TopFrame, font=('Tahoma',12, 'bold'), bd=1, width=20, justify = 'left',fg="Gray70")
        self.tboxPassword.insert(0, "Password...")
        self.tboxPassword.bind("<FocusIn>", temp_text_password)
        self.tboxPassword.grid(row = 2, column = 0, sticky=W, padx=5, pady=0)
        
        def Login():
            Username = self.tboxUsername.get()
            Password = self.tboxPassword.get()

            response = user_List.user_Login(Username, Password, db)

            if (response == "Username does not exist"):
                messagebox.showinfo("Login Error", "Username does not exist")

            elif (response == "Logged in successfully"):
                self.grid_remove()
                controller.show_frame(MainMenu)

            else:
                messagebox.showinfo("Login Error", "Incorrect password")


        #============================================BUTTONS===================================================#
        self.btnLogin = Button(ButtonFrame, font=('tahoma',16,'bold'), text = "Login", bd=2, width=10, height=2, command = Login).grid(row=0, column=0, padx=1)
        self.btnSignup = Button(ButtonFrame, font=('tahoma',16,'bold'), text = "Signup", bd=2, width=10, height=2, command = lambda : controller.show_frame(Signup)).grid(row=0, column=1, padx=1)

#============================================================================================================================================================================================================#  
class Signup(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # Title Frame
        TitleFrame_signup = Frame(self, bd = 7, width = 500, height = 300, bg = "#047857")
        TitleFrame_signup.grid(row = 0, column = 0)

        # Top Frame
        TopFrame_signup = Frame(self, bd = 0, width = 800, height = 500, relief = RIDGE)
        TopFrame_signup.grid(row = 1, column = 0)

        ButtonFrame_signup = Frame(self, bd = 0, width = 800, height = 500, padx=1, pady=1)
        ButtonFrame_signup.grid(row = 2, column = 0, padx=15, pady=15)

        #============================================TITLE AND LABELS==========================================#
        def temp_text_username(e):
            self.tboxUsername_signup.delete(0,"end")
            self.tboxUsername_signup.configure(fg="Black")

        def temp_text_password(e):
            self.tboxPassword_signup.delete(0,"end")
            self.tboxPassword_signup.configure(fg="Black")
        
        #Title Label
        self.lbltitle_signup = Label(TitleFrame_signup, font=('Tahoma',20, 'bold'), text = "Sign Up", bd=10, fg="white", bg="#047857")
        self.lbltitle_signup.grid(row = 0, column = 0, padx=95)

        # Username
        self.lblUsername_signup = Label(TopFrame_signup, text = "Username:",font=('Tahoma',12, 'bold'), bd=1, justify = 'center')
        self.lblUsername_signup.grid(row = 0, column = 0, sticky=W, padx=0, pady=0)
        self.tboxUsername_signup = Entry(TopFrame_signup, font=('Tahoma',12, 'bold'), bd=1, width=20, justify = 'left',fg="Gray70")
        self.tboxUsername_signup.bind("<FocusIn>", temp_text_username)
        self.tboxUsername_signup.grid(row = 0, column = 1, sticky=W, padx=5, pady=10)

        # Password
        self.lblPassword_signup = Label(TopFrame_signup, text = "Password:",font=('Tahoma',12, 'bold'), bd=1, justify = 'center')
        self.lblPassword_signup.grid(row = 1, column = 0, sticky=W, padx=0, pady=0)
        self.tboxPassword_signup = Entry(TopFrame_signup, font=('Tahoma',12, 'bold'), bd=1, width=20, justify = 'left',fg="Gray70")
        self.tboxPassword_signup.bind("<FocusIn>", temp_text_password)
        self.tboxPassword_signup.grid(row = 1, column = 1, sticky=W, padx=5, pady=0)
        
        def Create():
            Username = self.tboxUsername_signup.get()
            Password = self.tboxPassword_signup.get()
            
            if (Username == "") and (Password == ""):
                Username = self.tboxUsername_signup.get()
                Password = self.tboxPassword_signup.get()
                messagebox.showinfo("Sign-up Error", "Please enter a Username and Password")

            else:
                response = user_List.user_Create(Username, Password, db, conn)

                if (response == "Username is already taken"):
                    messagebox.showinfo("Sign-up Error", "Username is already taken")

                else:
                    messagebox.showinfo("Sign-up Success", "User Created")
                    self.grid_remove()
                    controller.show_frame(LoginPage)

        def Cancel():
            self.grid_remove()
            controller.show_frame(LoginPage)

        #============================================BUTTONS===================================================#
        self.btnCreate = Button(ButtonFrame_signup, font=('tahoma',16,'bold'), text = "Create", bd=2, width=10, height=2,command = Create).grid(row=0, column=0, padx=1)
        self.btnCancel = Button(ButtonFrame_signup, font=('tahoma',16,'bold'), text = "Cancel", bd=2, width=10, height=2, command = Cancel).grid(row=0, column=1, padx=1)

#============================================================================================================================================================================================================#
# second window frame mainmenu
class MainMenu(tk.Frame):
     
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        mainMenu_TitleFrame = Frame(self, bd = 0, width = 500, height = 300, bg = "#047857", padx=100, pady=25)
        mainMenu_TitleFrame.grid(row = 0, column = 0)
        mainMenu_ButtonFrame = Frame(self, bd = 0, width = 10000, height = 10000, padx=50, pady=50)
        mainMenu_ButtonFrame.grid(row = 1, column = 0, padx=0, pady=0)

        self.lblmainMenu = Label(mainMenu_TitleFrame, font=('Tahoma',30, 'bold'), text = "Main Menu", bd=10, fg="white", bg="#047857", padx=40, pady=0)
        self.lblmainMenu.grid(row = 0, column = 0)

        #============================================BUTTONS===================================================#
        def exit():
            controller.destroy()

        button_image_1 = PhotoImage(
            file='button_1.png')
        self.button_1 = Button(mainMenu_ButtonFrame,
            image=button_image_1,
            command=lambda: print("button_1 clicked"),
            padx=2000,
            pady=2000
        )
        self.button_1.image = button_image_1
        self.button_1.grid(row = 0, column = 0, padx=10, pady=10)

        button_image_2 = PhotoImage(
            file='button_2.png')
        self.button_2 = Button(mainMenu_ButtonFrame,
            image=button_image_2,
            command=lambda: print("button_2 clicked"),
            padx=2000,
            pady=2000
        )
        self.button_2.image = button_image_2
        self.button_2.grid(row = 1, column = 0, padx=10, pady=10)

        button_image_3 = PhotoImage(
            file='button_3.png')
        self.button_3 = Button(mainMenu_ButtonFrame,
            image=button_image_3,
            command=exit,
            padx=2000,
            pady=2000
        )
        self.button_3.image = button_image_3
        self.button_3.grid(row = 2, column = 0, padx=10, pady=10)

#============================================================================================================================================================================================================#
# third window frame page2
class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Page 2", font = LARGEFONT)
        label.grid(row = 0, column = 4, padx = 10, pady = 10)
  
        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text ="Page 1",
                            command = lambda : controller.show_frame(MainMenu))
     
        # putting the button in its place by
        # using grid
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)
  
        # button to show frame 3 with text
        # layout3
        button2 = ttk.Button(self, text ="LoginPage",
                            command = lambda : controller.show_frame(LoginPage))
     
        # putting the button in its place by
        # using grid
        button2.grid(row = 2, column = 1, padx = 10, pady = 10)
  
#============================================================================================================================================================================================================#
# Driver Code
if __name__ == '__main__':
    Initialize.initialize()
    app = tkinterApp()
    app.mainloop()