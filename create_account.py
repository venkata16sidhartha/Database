from tkinter import *
import os
account = Tk()
account.title('Create account')
first_name =StringVar()
middle_name=StringVar()
last_name=StringVar()
age=StringVar()
sex=StringVar()
date_of_birth=StringVar()
gmail=StringVar()
phone_number= StringVar()

def getvalue():
    f= open("temp.txt","w+")
    f.write(first_name.get())
    f.close()
    f=open("temp.txt","a+")
    f.write("\n")
    f.close()
    f=open("temp.txt","a+")
    f.write(middle_name.get())
    f.close()
    f=open("temp.txt","a+")
    f.write("\n")
    f.close()
    f=open("temp.txt","a+")
    f.write( last_name.get())
    f.close()
    f=open("temp.txt","a+")
    f.write("\n")
    f.close()
    f=open("temp.txt","a+")
    f.write( age.get())
    f.close()
    f=open("temp.txt","a+")
    f.write("\n")
    f.close()
    f=open("temp.txt","a+")
    f.write( sex.get())
    f.close()
    f=open("temp.txt","a+") 
    f.write("\n")
    f.close()
    f=open("temp.txt","a+") 
    f.write( date_of_birth.get())
    f.close()
    f=open("temp.txt","a+")
    f.write("\n")
    f.close()
    f=open("temp.txt","a+")
    f.write( gmail.get())
    f.close()
    f=open("temp.txt","a+")
    f.write("\n")
    f.close()
    f=open("temp.txt","a+")
    f.write( phone_number.get())
    f.close()
    os.system("python genpsswd.py")
def red():
    Label(account, text="phone number",bg='red').grid(row=2,column=2, sticky=W)
def green():
    Label(account, text="phone number",bg='white').grid(row=2,column=2, sticky=W)
    WSignUp1= Button(account, text="Save ", command =getvalue).grid(row=3, column=5, sticky=W)
def checkPN():
    j=str(phone_number.get())
    if(len(j)==10):
        for i in range(len(j)):
            if(j[i] not in ['1','2','3','4','5','6','7','8','9','0']):
                a=red()
                break;
            else:
                a=green()
    else:
        z=red()
Label(account, text="first name").grid(row=0, sticky=W)  #label
Entry(account, textvariable = first_name).grid(row=0, column=1, sticky=E) #entry textbox
Label(account, text="last name").grid(row=0,column=4, sticky=W)  #label
Entry(account, textvariable = last_name).grid(row=0, column=5, sticky=E) #entry textbox
Label(account, text="Age").grid(row=1,column=0, sticky=W)  #label
Entry(account, textvariable = age).grid(row=1, column=1, sticky=E) #entry textbox
Label(account, text="Sex").grid(row=1,column=2, sticky=W)  #label
Entry(account, textvariable = sex).grid(row=1, column=3, sticky=E) #entry textbox
Label(account, text="Date of birth").grid(row=1,column=4, sticky=W)  #label
Entry(account, textvariable = date_of_birth).grid(row=1, column=5, sticky=E) #entry textbox
Label(account, text="gmail").grid(row=2,column=0, sticky=W)  #label
Entry(account, textvariable = gmail).grid(row=2, column=1, sticky=E) #entry textbox
Label(account, text="phone number").grid(row=2,column=2, sticky=W)  #label
Entry(account,textvariable = phone_number).grid(row=2, column=3, sticky=E)#entry textbox
Label(account, text="middle name").grid(row=0,column=2, sticky=W)  #label
Entry(account, textvariable = middle_name).grid(row=0, column=3, sticky=E) #entry textbox
WSignUp3= Button(account, text="Check", command =checkPN).grid(row=3, column=0, sticky=W)

WSignUp2= Button(account, text="Done", command =quit).grid(row=3, column=1, sticky=W) #button

account.mainloop()
