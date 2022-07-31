from asyncio.windows_events import NULL
from cgitb import text
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from pathlib import Path

import user_List
import Initialize
import prediction_List

# Model Training Libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

db, conn = Initialize.db_create()
  
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
        for F in (LoginPage, MainMenu, Signup, ViewList, CreateEntry):
  
            frame = F(container, self)
  
            # initializing frame of that object from
            # LoginPage, MainMenu, Signup, ViewList, Create Entry respectively with
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
        self.configure(bg="#CFCFBC")
        # Title Frame
        TitleFrame = Frame(self, bd = 0, width = 535, height = 200, bg = "#3A4132")
        TitleFrame.grid(row = 0, column = 0)

        # BG Frame
        BGFrame = Frame(self, bd = 0, width = 535, height = 200)
        BGFrame.grid(row = 1, column = 0)

        #Title Label
        img2 = Image.open("images/lower_login_bg.PNG")
        resized2 = img2.resize((535,200), Image.ANTIALIAS)
        self.lower_login_img = ImageTk.PhotoImage(resized2)
        self.lower_login_bg = Label(BGFrame, image=self.lower_login_img, bg="#3A4132", bd=0)
        self.lower_login_bg.grid(row = 0, column = 0)

        # Top Frame
        TopFrame = Frame(BGFrame, bd = 0, width = 800, height = 500, relief = RIDGE, bg="#BFC89A")
        TopFrame.place(x=165, y=30)

        ButtonFrame = Frame(BGFrame, bd = 0, width = 800, height = 500, padx=1, pady=1,  bg="#BFC89A")
        ButtonFrame.place(x=177, y=120)

        #============================================TITLE AND LABELS==========================================#
        def temp_text_username(e):
            self.tboxUsername.delete(0,"end")
            self.tboxUsername.configure(fg="Black")

        def temp_text_password(e):
            self.tboxPassword.delete(0,"end")
            self.tboxPassword.configure(fg="Black")
        
        #Title Label
        img1 = Image.open("images/upper_login_bg.png")
        resized1 = img1.resize((535,200), Image.ANTIALIAS)
        self.upper_login_img = ImageTk.PhotoImage(resized1)
        self.upper_login_bg = Label(TitleFrame, image=self.upper_login_img, bg="#3A4132", anchor=NW, bd=0)
        self.upper_login_bg.place(x=0, y=0)

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

        def signup():
                self.grid_remove()
                controller.show_frame(Signup)

        #============================================BUTTONS===================================================#
        login_image = Image.open("images/Login_Button.png")
        resized_login = login_image.resize((70,30), Image.ANTIALIAS)
        loginbutton_image = ImageTk.PhotoImage(resized_login)
        self.btnLogin = Button(ButtonFrame, bd=0,
            image=loginbutton_image,
            command=Login,
        )
        self.btnLogin.image = loginbutton_image
        self.btnLogin.grid(row = 0, column = 0, padx=10)

        signup_image = Image.open("images/Signup_Button.png")
        resized_signup = signup_image.resize((70,30), Image.ANTIALIAS)
        signupbutton_image = ImageTk.PhotoImage(resized_signup)
        self.btnSignup = Button(ButtonFrame, bd=0,
            image=signupbutton_image,
            command=signup,
        )
        self.btnSignup.image = signupbutton_image
        self.btnSignup.grid(row = 0, column = 1, padx=10)

#============================================================================================================================================================================================================#  
class Signup(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # Title Frame
        self.configure(bg="#CFCFBC")
        TitleFrame_signup = Frame(self, bd = 0, width = 535, height = 200, bg = "#3A4132")
        TitleFrame_signup.grid(row = 0, column = 0)

        # Top Frame
        TopFrame_signup = Frame(self, bd = 0, width = 800, height = 500, relief = RIDGE, bg="#CFCFBC")
        TopFrame_signup.grid(row = 1, column = 0)

        ButtonFrame_signup = Frame(self, bd = 0, width = 800, height = 100, bg="#CFCFBC")
        ButtonFrame_signup.grid(row = 2, column = 0, padx=15, pady=15)

        #============================================TITLE AND LABELS==========================================#
        #Title Label
        img1 = Image.open("images/signup_bg.jpg")
        resized1 = img1.resize((535,200), Image.ANTIALIAS)
        self.signup_img = ImageTk.PhotoImage(resized1)
        self.signup_bg = Label(TitleFrame_signup, image=self.signup_img, bg="#3A4132", anchor=NW, bd=0)
        self.signup_bg.place(x=0, y=0)

        def temp_text_username(e):
            self.tboxUsername_signup.delete(0,"end")
            self.tboxUsername_signup.configure(fg="Black")

        def temp_text_password(e):
            self.tboxPassword_signup.delete(0,"end")
            self.tboxPassword_signup.configure(fg="Black")

        # Username
        self.lblUsername_signup = Label(TopFrame_signup, text = "Username:",font=('Tahoma',12, 'bold'), bd=1, justify = 'center', bg="#CFCFBC")
        self.lblUsername_signup.grid(row = 0, column = 0, sticky=W, padx=0, pady=0)
        self.tboxUsername_signup = Entry(TopFrame_signup, font=('Tahoma',12, 'bold'), bd=1, width=20, justify = 'left',fg="Gray70")
        self.tboxUsername_signup.bind("<FocusIn>", temp_text_username)
        self.tboxUsername_signup.grid(row = 0, column = 1, sticky=W, padx=5, pady=10)

        # Password
        self.lblPassword_signup = Label(TopFrame_signup, text = "Password:",font=('Tahoma',12, 'bold'), bd=1, justify = 'center', bg="#CFCFBC")
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
        self.btnCreate = ttk.Button(ButtonFrame_signup, text = "Create", width=10, command = Create).grid(row=0, column=0, padx=10)
        self.btnCancel = ttk.Button(ButtonFrame_signup, text = "Cancel", width=10, command = Cancel).grid(row=0, column=1, padx=10)

#============================================================================================================================================================================================================#
# second window frame mainmenu
class MainMenu(tk.Frame):
     
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(bg="#BFC89A")

        mainMenu_TitleFrame = Frame(self, bd = 0, width = 400, height = 200, bg = "#3A4132", padx=0, pady=0)
        mainMenu_TitleFrame.grid(row = 0, column = 0)
        mainMenu_ButtonFrame = Frame(self, bd = 0, width = 10000, height = 10000, padx=0, pady=20, bg="#BFC89A")
        mainMenu_ButtonFrame.grid(row = 1, column = 0, padx=0, pady=0)

        #Title Label
        img1 = Image.open("images/mainmenu_bg.jpg")
        resized1 = img1.resize((400,200), Image.ANTIALIAS)
        self.mainmenu_img = ImageTk.PhotoImage(resized1)
        self.mainmenu_bg = Label(mainMenu_TitleFrame, image=self.mainmenu_img, bg="#3A4132", anchor=NW, bd=0)
        self.mainmenu_bg.place(x=0, y=0)

        #============================================BUTTONS===================================================#
        def exit():
            controller.destroy()

        def viewlist():
            self.grid_remove()
            controller.show_frame(ViewList)

        def createentry():
            self.grid_remove()
            controller.show_frame(CreateEntry)

        img1 = Image.open("images/CreateEntry_btn.png")
        resized1 = img1.resize((200,90), Image.ANTIALIAS)
        CreateEntry_btn_img = ImageTk.PhotoImage(resized1)
        self.CreateEntry_btn = Button(mainMenu_ButtonFrame,
            image=CreateEntry_btn_img,
            command=createentry,
            bd=0
        )
        self.CreateEntry_btn.image = CreateEntry_btn_img
        self.CreateEntry_btn.grid(row = 0, column = 0, padx=10, pady=10)

        img2 = Image.open("images/ViewList_btn.png")
        resized2 = img2.resize((200,70), Image.ANTIALIAS)
        ViewList_btn_img = ImageTk.PhotoImage(resized2)
        self.ViewList_btn = Button(mainMenu_ButtonFrame,
            image=ViewList_btn_img,
            command=viewlist,
            bd=0
        )
        self.ViewList_btn.image = ViewList_btn_img
        self.ViewList_btn.grid(row = 1, column = 0, padx=10, pady=10)

        img3 = Image.open("images/Exit_btn.png")
        resized3 = img3.resize((200,70), Image.ANTIALIAS)
        Exit_btn_img = ImageTk.PhotoImage(resized3)
        self.Exit_btn = Button(mainMenu_ButtonFrame,
            image=Exit_btn_img,
            command=exit,
            bd=0
        )
        self.Exit_btn.image = Exit_btn_img
        self.Exit_btn.grid(row = 2, column = 0, padx=10, pady=10)

#============================================================================================================================================================================================================#
# third window frame ViewList
class ViewList(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(bg="#818964")

        # Title Frame
        TitleFrame = Frame(self, bd = 7, width = 500, height = 300, bg = "#68704B")
        TitleFrame.grid(row = 0, column = 0)

        # Top Frame
        TopFrame = Frame(self, bd = 0, width = 200, height = 200, relief = RIDGE)
        TopFrame.grid(row = 1, column = 0, pady=20, padx=10)

        # Button Frame
        ButtonFrame = Frame(self, bd = 0, width = 800, height = 500, padx=1, pady=1, bg="#818964")
        ButtonFrame.grid(row = 3, column = 0, padx=15, pady=15)

        # Add Record Entry Boxes
        data_frame = LabelFrame(self, text="Record", bg="#818964")
        data_frame.grid(row=2, column=0, padx=20)

        fn_label = Label(data_frame, text="First Name", bg="#818964", anchor=E)
        fn_label.grid(row=0, column=0, padx=10, pady=10)
        fn_entry = Entry(data_frame)
        fn_entry.grid(row=0, column=1, padx=10, pady=10)

        ln_label = Label(data_frame, text="Last Name", bg="#818964", anchor=E)
        ln_label.grid(row=0, column=2, padx=10, pady=10)
        ln_entry = Entry(data_frame)
        ln_entry.grid(row=0, column=3, padx=10, pady=10)

        id_label = Label(data_frame, text="ID", bg="#818964", anchor=E)
        id_label.grid(row=0, column=4, padx=10, pady=10)
        id_entry = Entry(data_frame)
        id_entry.grid(row=0, column=5, padx=10, pady=10)

        address_label = Label(data_frame, text="Address", bg="#818964", anchor=E)
        address_label.grid(row=1, column=0, padx=10, pady=10)
        address_entry = Entry(data_frame)
        address_entry.grid(row=1, column=1, padx=10, pady=10)

        contactnum_label = Label(data_frame, text="Contact Number", bg="#818964", anchor=E)
        contactnum_label.grid(row=1, column=2, padx=10, pady=10)
        contactnum_entry = Entry(data_frame)
        contactnum_entry.grid(row=1, column=3, padx=10, pady=10)

        prediction_label = Label(data_frame, text="Prediction", bg="#818964", anchor=E)
        prediction_label.grid(row=1, column=4, padx=10, pady=10)
        prediction_entry = Entry(data_frame)
        prediction_entry.grid(row=1, column=5, padx=10, pady=10)


        self.lblviewlist= Label(TitleFrame, font=('Century',24, 'bold'), text = "Prediction List", bd=10, fg="white", bg="#68704B", padx=10, pady=0)
        self.lblviewlist.grid(row = 0, column = 0, padx=250)

        # Add Some Style
        style = ttk.Style()

        # Pick A Theme
        style.theme_use('clam')

        # Configure the Treeview Colors
        style.configure("Treeview",
            background="#D3D3D3",
            foreground="black",
            rowheight=25,
            fieldbackground="#D3D3D3")

        # Change Selected Color
        style.map('Treeview',
	        background=[('selected', "#047857")])

        # Tree View
        self.tree = ttk.Treeview(master = TopFrame, columns=("ID", "First Name", "Last Name", "Address", "Contact Number", "Prediction"))
        self.tree.pack(side=LEFT)

        self.tree.column("#0", width=0, stretch=NO)
        self.tree.column("First Name", anchor=CENTER, width=120, minwidth=25)
        self.tree.column("Last Name", anchor=CENTER, width=120, minwidth=25)
        self.tree.column("ID", anchor=CENTER, width=100)
        self.tree.column("Address", anchor=CENTER, width=120, minwidth=25)
        self.tree.column("Contact Number", anchor=CENTER, width=120, minwidth=25)
        self.tree.column("Prediction", anchor=CENTER, width=120, minwidth=25)

        self.tree.heading("#0", text="", anchor=W)
        self.tree.heading("First Name", text="First Name", anchor=CENTER)
        self.tree.heading("Last Name", text="Last Name", anchor=CENTER)
        self.tree.heading("ID", text="ID", anchor=CENTER)
        self.tree.heading("Address", text="Address", anchor=CENTER)
        self.tree.heading("Contact Number", text="Contact Number", anchor=CENTER)
        self.tree.heading("Prediction", text="Prediction", anchor=CENTER)

        # Create Striped Row Tags
        self.tree.tag_configure('oddrow', background="#565F36")
        self.tree.tag_configure('evenrow', background="#E3EBC3")

        self.scrollbar = Scrollbar(TopFrame, orient=VERTICAL)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.scrollbar.config(command=self.tree.yview, bd=2, relief=RIDGE)

        # button to show frame 2 with text
        # layout2

        data = prediction_List.entry_CheckList(db)
        numid = 1
        for record in data:
            if numid % 2 == 0:
                self.tree.insert(parent='', index='end', iid=numid, text='', values=(numid, record[0], record[1], record[2], record[3], record[4]), tags=('evenrow',))
            else:
                self.tree.insert(parent='', index='end', iid=numid, text='', values=(numid, record[0], record[1], record[2], record[3], record[4]), tags=('oddrow',))
            # increment counter
            numid = numid + 1

        def refresh():
            for record in self.tree.get_children():
                self.tree.delete(record)

            data = prediction_List.entry_CheckList(db)
            numid = 1
            for record in data:
                if numid % 2 == 0:
                    self.tree.insert(parent='', index='end', iid=numid, text='', values=(numid, record[0], record[1], record[2], record[3], record[4]), tags=('evenrow',))
                else:
                    self.tree.insert(parent='', index='end', iid=numid, text='', values=(numid, record[0], record[1], record[2], record[3], record[4]), tags=('oddrow',))
                # increment counter
                numid = numid + 1

        # Remove one record
        def delete_record():
            x = self.tree.selection()[0]
            # Grab record Number
            selected = self.tree.focus()
            # Grab record values
            values = self.tree.item(selected, 'values')
            prediction_List.entry_Delete(values[1], values[2], db, conn)
            self.tree.delete(x)
            refresh()

        # Select Record
        def select_record():
            # Clear entry boxes
            fn_entry.delete(0, END)
            ln_entry.delete(0, END)
            id_entry.delete(0, END)
            address_entry.delete(0, END)
            contactnum_entry.delete(0, END)
            prediction_entry.delete(0, END)

            # Grab record Number
            selected = self.tree.focus()
            # Grab record values
            values = self.tree.item(selected, 'values')

            # outpus to entry boxes
            fn_entry.insert(0, values[1])
            ln_entry.insert(0, values[2])
            id_entry.insert(0, values[0])
            address_entry.insert(0, values[3])
            contactnum_entry.insert(0, values[4])
            prediction_entry.insert(0, values[5])

        # Update record
        def update_record():
            # Grab the record number
            selected = self.tree.focus()
            # Grab record Number
            selected = self.tree.focus()
            # Grab record values
            values = self.tree.item(selected, 'values')
            firstname_old = values[1]
            lastname_old = values[2]
            # Update Database
            prediction_List.entry_Edit(firstname_old, lastname_old, fn_entry.get(), ln_entry.get(), contactnum_entry.get(), address_entry.get(), prediction_entry.get(), db, conn)
            # Update record
            #self.tree.item(selected, text="", values=(fn_entry.get(), ln_entry.get(), id_entry.get(), address_entry.get(), contactnum_entry.get(), prediction_entry.get()))
            refresh()



            # Clear entry boxes
            fn_entry.delete(0, END)
            ln_entry.delete(0, END)
            id_entry.delete(0, END)
            address_entry.delete(0, END)
            contactnum_entry.delete(0, END)
            prediction_entry.delete(0, END)

        def back2mainmenu():
            self.grid_remove()
            refresh()
            controller.show_frame(MainMenu)

        def refresh_record():
            refresh()

        # Add Buttons
        button_frame = LabelFrame(ButtonFrame, text="Commands", bg="#818964")
        button_frame.pack(fill="x", expand="yes", padx=20)

        img2 = Image.open("images/update_btn.png")
        resized2 = img2.resize((100,45), Image.ANTIALIAS)
        update_btn_img = ImageTk.PhotoImage(resized2)
        self.update_btn = Button(button_frame,
            image=update_btn_img,
            command=update_record,
            bd=0
        )
        self.update_btn.image = update_btn_img
        self.update_btn.grid(row = 0, column = 0, padx=10, pady=10)

        img3 = Image.open("images/delete_btn.png")
        resized3 = img3.resize((100,45), Image.ANTIALIAS)
        delete_btn_img = ImageTk.PhotoImage(resized3)
        self.delete_btn = Button(button_frame,
            image=delete_btn_img,
            command=delete_record,
            bd=0
        )
        self.delete_btn.image = delete_btn_img
        self.delete_btn.grid(row = 0, column = 1, padx=10, pady=10)

        img4 = Image.open("images/edit_btn.png")
        resized4 = img4.resize((100,45), Image.ANTIALIAS)
        edit_btn_img = ImageTk.PhotoImage(resized4)
        self.edit_btn = Button(button_frame,
            image=edit_btn_img,
            command=select_record,
            bd=0
        )
        self.edit_btn.image = edit_btn_img
        self.edit_btn.grid(row = 0, column = 2, padx=10, pady=10)

        img5 = Image.open("images/Refresh_btn.png")
        resized5 = img5.resize((100,45), Image.ANTIALIAS)
        Refresh_btn_img = ImageTk.PhotoImage(resized5)
        self.Refresh_btn = Button(button_frame,
            image=Refresh_btn_img,
            command=refresh_record,
            bd=0
        )
        self.Refresh_btn.image = Refresh_btn_img
        self.Refresh_btn.grid(row = 0, column = 3, padx=10, pady=10)

        img1 = Image.open("images/imgdesign5.png")
        resized1 = img1.resize((20,20), Image.ANTIALIAS)
        imgbackbutton_design = ImageTk.PhotoImage(resized1)
        self.back_button = Button(TitleFrame, font=("Tahoma", 12), width=75, anchor=CENTER, image=imgbackbutton_design, text='Back', compound=tk.LEFT, command=back2mainmenu, bg="#818066")
        self.back_button.image = imgbackbutton_design
        self.back_button.place(x=20, y=10)

class CreateEntry(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path("./images/assets")


        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)        

        mainframe = Frame(self)
        mainframe.grid()

        # Canvas
        canvas = Canvas( mainframe, bg = "#CFCFBC", height = 850, width = 800, bd = 0, highlightthickness = 0, relief = "ridge" ) 
        canvas.place(x = 0, y = 0) 
        canvas.create_rectangle( 18.0, 154.0, 871.0, 158.0, fill="#3A4132", outline="")

        # Right Frame
        canvas.create_rectangle( 525.0, 170.0, 773.0, 813.0, fill="#3A4132", outline="")
        canvas.create_text( 549.0, 303.0, anchor="nw", text="Analysis:", fill="#FFFFFF", font=("Arial Bold", 14 * -1) ) 
        Label(canvas, text="                    Summary\nFirst Name: \n\n\nLast Name: \n\n\nAddress \n\n\nContact Number \n\n\nPredction", fg = "#FFFFFF", bg = "#3A4132", justify = 'left', font=("Arial Bold", 14 * -1)).place(x=549.0, y=370.0)
        Label(canvas, text="Dataset:\nHeart Attack Analysis &\nPrediction Dataset\n By: RASHIK RAHMAN", fg = "#FFFFFF", bg = "#3A4132", font=("Arial Bold", 14 * -1)).place(x=565.0, y=720.0)


        # Title
        canvas.create_rectangle(0.0,0.0,882.0,56.0,fill="#3A4132",outline="")
        canvas.create_text( 19.0, 81.0, anchor="nw", text="Elderly Heart Health Monitoring Application", fill="#000000", font=("Arial Bold", 33 * -1) ) 
        canvas.create_text( 19.0, 124.0, anchor="nw", text="Allorde - Del Rosario - Valeriano", fill="#000000", font=("Arial Regular", 20 * -1) )


        # Image
        heart1Image = PhotoImage(file="images/heart1.png")
        heart1 = canvas.create_image(638.0,240.0,image=heart1Image)

        # Age
        canvas.create_text(22.0,164.0,anchor="nw",text="Age",fill="#000000",font=("Arial Bold", 14 * -1))
        ageImage = PhotoImage(file=relative_to_assets("dataTextbox.png"))
        canvas.create_image(117.0,199.5,image=ageImage)
        ageEntry = Entry(mainframe,bd=0,bg="#FFFFFF",highlightthickness=0)
        ageEntry.place(x=27.0,y=187.0,width=178.0,height=23.0)

        # Sex
        canvas.create_text(22.0,226.0,anchor="nw",text="Sex",fill="#000000",font=("Arial Bold", 14 * -1))
        sexVar = StringVar(mainframe)
        sexVar.set("Select Option")
        sexOM = OptionMenu(mainframe, sexVar,"Male","Female")
        sexOM.pack()
        sexOM.place(x=22.0,y=250.0,width=185.0,height=38.0)

        # Chest Pain Type
        canvas.create_text(22.0,295.0,anchor="nw",text="Chest Pain Type",fill="#000000",font=("ArialBold", 14 * -1))
        cpVar = StringVar(mainframe)
        cpVar.set("Select Option")
        cpOM = OptionMenu(mainframe, cpVar,"typical angina","atypical angina","non-anginal pain","asymptomatic")
        cpOM.pack()
        cpOM.place(x=22.0,y=320.0,width=185.0,height=38.0)

        # Resting Blood Pressure
        canvas.create_text(22.0,368.0,anchor="nw",text="Resting Blood Pressure",fill="#000000",font=("Arial Bold", 14 * -1))
        trtbpsImage = PhotoImage(file=relative_to_assets("dataTextbox.png"))
        trtbpsBg = canvas.create_image(111.0,403.0,image=trtbpsImage)
        trtbpsEntry = Entry(mainframe, bd=0,bg="#FFFFFF",highlightthickness=0)
        trtbpsEntry.place(x=27.0,y=391.0,width=178.0,height=23.0)


        # Cholesterol in mg/dl
        canvas.create_text( 22.0, 425.0, anchor="nw", text="Cholesterol in mg/dl", fill="#000000", font=("Arial Bold", 14 * -1) ) 
        cholImage = PhotoImage(file=relative_to_assets("dataTextbox.png"))
        cholBg = canvas.create_image(111.0,461.5,image=cholImage)
        cholEntry = Entry(mainframe, bd=0,bg="#FFFFFF",highlightthickness=0)
        cholEntry.place(x=27.0,y=449.0,width=180.0,height=23.0)


        # Fasting Blood Sugar
        canvas.create_text(22.0,482.0,anchor="nw",text="Fasting Blood Sugar",fill="#000000",font=("Arial Bold", 14 * -1))
        fbsVar = StringVar(mainframe)
        fbsVar.set("Select Option")
        fbsOM = OptionMenu(mainframe, fbsVar,"FBS >= 120 mg/dl","FBS < 120 mg/dl")
        fbsOM.place(x=22.0,y=500.0,width=185.0,height=38.0)

        # Resting Electrocardiographic Results
        canvas.create_text(22.0,555.0,anchor="nw",text="Resting Electrocardiographic Value",fill="#000000",font=("Arial Bold", 14 * -1))
        rest_ecgVar = StringVar(mainframe)
        rest_ecgVar.set("Select Option")
        rest_ecgOM = OptionMenu(mainframe, rest_ecgVar,"normal","ST-T wave abnormality","left ventricular hypertrophy")
        rest_ecgOM.pack()
        rest_ecgOM.place(x=22.0,y=586.0,width=185.0,height=38.0)


        # Maximum Heart Rate
        canvas.create_text( 25.0, 631.0, anchor="nw", text="Maximum Heart rate", fill="#000000", font=("Arial Bold", 14 * -1) )
        thalachImage = PhotoImage(file=relative_to_assets("dataTextbox.png"))
        thalachBg = canvas.create_image( 117.0, 665.5, image=thalachImage)
        thalachEntry = Entry(mainframe, bd=0, bg="#FFFFFF", highlightthickness=0)
        thalachEntry.place(x=27.0,y=653.0,width=180.0,height=23.0)


        # Exercise Induced Angina
        canvas.create_text(22.0,692.0,anchor="nw",text="Exercise Induced Angina",fill="#000000",font=("Arial Bold", 14 * -1))
        exangVar = StringVar(mainframe)
        exangVar.set("Select Option")
        exangOM = OptionMenu(mainframe, exangVar,"Yes","No")
        exangOM.pack()
        exangOM.place(x=22.0,y=710.0,width=185.0,height=38.0)

        # Precious Peak
        canvas.create_text( 28.0, 759.0, anchor="nw", text="Previous Peak", fill="#000000", font=("Arial Bold", 14 * -1) )
        oldImage = PhotoImage(file=relative_to_assets("dataTextbox.png"))
        oldBg = canvas.create_image(117.0, 796.1, image=oldImage) 
        oldpeakEntry = Entry(mainframe, bd=0, bg="#FFFFFF", highlightthickness=0 ) 
        oldpeakEntry.place( x=27.0, y=783.0, width=180.0, height=23.0 )

 
        #Last Name
        canvas.create_text( 284.0, 166.0, anchor="nw", text="Last name", fill="#000000", font=("Arial Bold", 14 * -1) )
        gImage = PhotoImage(file=relative_to_assets("greenTextbox.png")) 
        lnBg = canvas.create_image(393.5, 205.0, image=gImage) 
        lnEntry = Entry(mainframe, bd=0, bg="#FFFFFF", highlightthickness=0) 
        lnEntry.place( x=286.0, y=194.0, width=217.0, height=23.0)

        # First Name
        canvas.create_text( 284.0, 223.0, anchor="nw", text="First name", fill="#000000", font=("Arial Bold", 14 * -1) )
        fnImage = canvas.create_image(393.5, 255.5, image=gImage)
        fnEntry = Entry(mainframe, bd=0, bg="#FFFFFF", highlightthickness=0 )
        fnEntry.place(x=286.0,y=244.0,width=217.0,height=23.0)


        # Address
        canvas.create_text( 284.0, 279.0, anchor="nw", text="Address", fill="#000000", font=("Arial Bold", 14 * -1) )
        addressImage = canvas.create_image(393.5, 315.0, image=gImage)
        addressEntry = Entry(mainframe, bd=0, bg="#FFFFFF", highlightthickness=0 )
        addressEntry.place(x=286.0,y=305.0,width=217.0,height=23.0)


        # Emergency Contact Number
        canvas.create_text(284.0, 337.0, anchor="nw", text="Emergency Contact Number", fill="#000000", font=("Arial Bold", 14 * -1) ) 
        numberImage = canvas.create_image(392.5, 370.0, image=gImage)
        numberEntry = Entry(mainframe, bd=0, bg="#FFFFFF", highlightthickness=0 )
        numberEntry.place(x=286.0,y=358.0,width=216.0,height=23.0)


        # Number of Major Vessels
        canvas.create_text(288.0,587.0,anchor="nw",text="Number of Major Vessels",fill="#000000",font=("Arial Bold", 14 * -1))
        caImage = PhotoImage(file=relative_to_assets("dataTextbox.png"))
        caBg = canvas.create_image(384.0,625.0,image=caImage)
        caEntry = Entry(bd=0,bg="#FFFFFF",highlightthickness=0)
        caEntry.place(x=294.0,y=610.0,width=180.0,height=23.0)

        # Thal Rate
        canvas.create_text( 288.0, 661.0, anchor="nw", text="Thal Rate", fill="#000000", font=("Arial Bold", 14 * -1) )
        thallImage = PhotoImage( file=relative_to_assets("dataTextbox.png")) 
        thallBg = canvas.create_image(384.0, 702.5, image=thallImage ) 
        thallEntry = Entry(mainframe, bd=0, bg="#FFFFFF", highlightthickness=0 ) 
        thallEntry.place( x=294.0, y=690.0, width=180.0, height=23.0 )

        # Slope
        canvas.create_text(286.0,530.0,anchor="nw",text="Slope",fill="#000000",font=("Arial Bold", 14 * -1))
        slpImage = PhotoImage( file=relative_to_assets("dataTextbox.png")) 
        slpBg = canvas.create_image(384.0, 565.5, image=slpImage ) 
        slpEntry = Entry(mainframe, bd=0, bg="#FFFFFF", highlightthickness=0 )
        slpEntry.place( x=294.0, y=553.0, width=180.0, height=23.0 )

        # Check Input
        def showError(error):
            messagebox.showerror('Input Error', 'Please Enter ' + error)
            return 0

        # Predict Model
        def predictHeart():
            # Data Collection and Processing
            HeartAttackAPdataset = pd.read_csv('Heart Attack Analysis.csv')
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
            print(training_data_accuracy)

            # Accuracy Score Test Data
            X_test_prediction = model.predict(X_test)
            test_data_accuracy = accuracy_score(X_test_prediction, Y_test)
            print(test_data_accuracy)


            # Get Data from Textbox and Dropdown Widgets

            stringAge = ageEntry.get()
            if stringAge == '':
                showError('Age')
            else:
                age = np.array(stringAge, dtype= int)

            sexOP = sexVar.get()
            if sexOP == "Male":
                sex = np.array(1, dtype= int)
            elif sexOP == "Female":
                sex = np.array(0, dtype= int)
            else:
                showError('Sex')

            cpOP = cpVar.get()
            if cpOP == "typical angina":
                cp = np.array(0, dtype= int)
            elif cpOP == "atypical angina":
                cp = np.array(1, dtype= int)
            elif cpOP == "non-anginal pain":
                cp = np.array(2, dtype= int)
            elif cpOP == "asymptomatic":
                cp = np.array(3, dtype= int)   
            else:
                showError('Chest Pain Type')

            stringTrtbps = trtbpsEntry.get()
            if stringTrtbps == '':
                showError('Resting Blood Pressure')
            else:
                trtbps = np.array(stringTrtbps, dtype= int)

            stringChol = cholEntry.get()
            if stringChol == '':
                showError('Cholesterol in mg/dl')
            else:
                chol = np.array(stringChol, dtype= int)

            fbsOP = fbsVar.get()
            if fbsOP == "FBS >= 120 mg/dl":
                fbs = np.array(1, dtype= int)
            elif fbsOP == "FBS < 120 mg/dl":
                fbs = np.array(0, dtype= int)
            else:
                showError('Fasting Blood Sugar')

            rest_ecgOP = rest_ecgVar.get()
            if rest_ecgOP == "normal":
                rest_ecg = np.array(0, dtype= int)
            elif rest_ecgOP == "ST-T wave abnormality":
                rest_ecg = np.array(1, dtype= int)
            elif rest_ecgOP == "left ventricular hypertrophy":
                rest_ecg = np.array(2, dtype= int)
            else:
                showError('Resting Electrocardiographic Value')
            
            stringThalach = thalachEntry.get()
            if stringThalach == '':
                showError('Maximum Heart Rate')
            else:
                thalach = np.array(stringThalach, dtype= int)

            exangOP = exangVar.get()
            if exangOP == "Yes":
                exang = np.array(1, dtype= int)
            elif exangOP == "No":
                exang = np.array(0, dtype= int)
            else:
                showError('Exercise Induced Angina')

            stringOldpeak = oldpeakEntry.get()
            if stringOldpeak == '':
                showError('Previous Peak')
            else:
                oldpeak = np.array(stringOldpeak, dtype= float)

            stringSlp = slpEntry.get()
            if stringSlp == '':
                showError('Slope')
            else:
                slp = np.array(stringSlp, dtype= float)

            stringCa = caEntry.get() ###
            if stringCa == '':
                showError('Number of Major Vessels')
            else:
                ca = np.array(stringCa, dtype= int)

            stringThall = thallEntry.get()
            if stringThall == '':
                showError('Thal Rate')
            else:
                thall = np.array(stringThall, dtype= float)

            # Personal Information
            fn = fnEntry.get()
            if fn == '':
                showError('First Name')
            ln = lnEntry.get()
            if ln == '':
                showError('Last Name')
            address = addressEntry.get()
            if address == '':
                showError('Addres')
            number = numberEntry.get()
            if number == '':
                showError('Number')

            # Create input data list
            inputData = (age,sex,cp,trtbps,chol,fbs,rest_ecg,thalach,exang,oldpeak,slp,ca,thall)
            print(inputData)

            # Change the input data to a numpy array
            dataToArray= np.asarray(inputData)

            # Reshape the numpy array as we are predicting for only on instance
            inputDataReshaped = dataToArray.reshape(1,-1)

            prediction = model.predict(inputDataReshaped)
            print(prediction)

            # Display Output
            if prediction[0]== 0:
                output = "No"
                outputResult1 = "The The Person does not \nhave a Heart Disease"
                outputResult2 = "Continue Having\na Healthy Life"

            else:
                output = "Yes"
                outputResult1 = "The Person has \nHeart Disease"
                outputResult2 = "Please Contact/\nConsult your Doctor"

            Label(canvas, text= outputResult1, fg = "#FFFFFF", bg = "#3A4132", font=("Arial Bold", 14 * -1)).place(x=570.0, y=327.0)
            Label(canvas, text=outputResult2, fg = "#FFFFFF", bg = "#3A4132", font=("Arial Bold", 14 * -1)).place(x=580.0, y=630.0)
            Label(canvas, text=fn, fg = "#FFFFFF", bg = "#3A4132", font=("Arial Bold", 14 * -1)).place(x=580.0, y=408.0)
            Label(canvas, text=ln, fg = "#FFFFFF", bg = "#3A4132", font=("Arial Bold", 14 * -1)).place(x=580.0, y=454.0)
            Label(canvas, text=address, fg = "#FFFFFF", bg = "#3A4132", font=("Arial Bold", 14 * -1)).place(x=580.0, y=502.0)
            Label(canvas, text=number, fg = "#FFFFFF", bg = "#3A4132", font=("Arial Bold", 14 * -1)).place(x=580.0, y=549.0)
            Label(canvas, text=output, fg = "#FFFFFF", bg = "#3A4132", font=("Arial Bold", 14 * -1)).place(x=580.0, y=596.0)

            lastname = lnEntry.get()
            firstname = fnEntry.get()
            address = addressEntry.get()
            number = numberEntry.get()

            prediction_List.entry_Create(firstname, lastname, output, address, number, db, conn)

        def back2mainmenu():
            self.grid_remove()
            controller.show_frame(MainMenu)

        img1 = Image.open("images/assets/button_1.png")
        resized1 = img1.resize((188, 35), Image.ANTIALIAS)
        predictImage = ImageTk.PhotoImage(resized1)
        predictButt = Button(mainframe, image=predictImage, borderwidth=0, highlightthickness=0, command=predictHeart, relief="flat")
        predictButt.image = predictImage
        predictButt.place(x=286.0, y=774.0)

        # Back Button
        img2 = Image.open("images/assets/button_2.png")
        resized2 = img2.resize((80, 24), Image.ANTIALIAS)
        backImage = ImageTk.PhotoImage(resized2)
        backButton = Button(mainframe, image=backImage, borderwidth=0, highlightthickness=0, command=back2mainmenu, relief="flat" ) 
        backButton.image = backImage
        backButton.place(x=12.0, y=12.0)
        
        canvas.pack()
        mainframe.grid()

#============================================================================================================================================================================================================#
# Driver Code
if __name__ == '__main__':
    Initialize.initialize()
    app = tkinterApp()
    app.mainloop()