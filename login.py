from tkinter import *
import sqlite3
login=Tk()
conn=sqlite3.connect('database.db')
c=conn.cursor()
import os
def check_credentials(usrnm,pswd):
    username=usrnm
    password=pswd
    c.execute("SELECT User_name,Password FROM stuffToPlot WHERE User_name='usenm'")
    for row in c.fetchall():
        print(row)
def otp(usrnm,pswd):
    #os.system('python generate_random_password.py')
    z=check_credentials(usrnm,pswd)
login.title("Login")
Label(login, text="User Name").grid(row=0,column=0 ,sticky=W) 
usrnm=Entry(login).grid(row=0, column=1, sticky=E) 
Label(login, text="Password").grid(row=1,column=0, sticky=W)  
pswd=Entry(login).grid(row=1, column=1, sticky=E)
Otpbutton= Button(login, text="Request One Time Password",command=otp(usrnm,pswd)).grid(row=5, column=0, sticky=W)
Label(login, text="OTP").grid(row=4,column=0, sticky=W) 
Entry(login).grid(row=4, column=1, sticky=E)
LoginButton= Button(login, text="Login",command=otp(usrnm,pswd)).grid(row=4, column=0, sticky=W)
login.mainloop()
