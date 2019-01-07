import  sqlite3
import os
import numpy as np
conn=sqlite3.connect('C:\\Users\\Sidhartha\\Desktop\\python\\database\\database.db')
c= conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS stuffToPlot(FirstName TEXT, MiddleName TEXT ,LastName TEXT ,Age TEXT ,Sex TEXT,Date_of_Birth TEXT,Gmail TEXT,Phone_number TEXT,User_name TEXT,Password TEXT)')
    
def create_account():
    os.system('python create_account.py') 
    os.system('python data_entry.py')
    os.remove("temp.txt")
    
def login():
    os.system('python login.py')
create_table()

    
from tkinter import *
from tkinter import messagebox
main_window = Tk()
main_window.title("login database")
main_window.iconbitmap('C:\\Users\\Sidhartha\\Desktop\\python\\database\\images\\Dapino-Medical-Heart-beat.ico')
C = Canvas(main_window, bg="blue", height=700, width=1250)
filename = PhotoImage(file ="C:\\Users\\Sidhartha\\Desktop\python\database\images\medical-background-with-loop_n26ve-_yg__F0005.png")
background_label = Label(main_window, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1) 
b = Button(main_window, text="OK",width=10,bg="purple")
b.place(relx=.1, rely=.1, anchor="c")
button = Button(main_window, 
                   text="Create Account", 
                   fg="red",
                   bg="lightblue",
                   command=create_account)
button.place(relx=.9,rely=.125)
login = Button(main_window, 
                   text="login", 
                   fg="black",
                   bg="grey",
                   command=login)
login.place(relx=.9,rely=.05)

 

C.pack()
main_window.mainloop()
