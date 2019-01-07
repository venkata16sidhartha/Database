from tkinter import *
import random
import os
filepath = 'temp.txt'
a=[]
with open(filepath) as fp:  
    line = fp.readline()
    cnt = 1
    
    while line:
         a.append(line.strip())
         line = fp.readline()
         cnt += 1
r=random.randint(1000,9999)
ra=["psswd",str(r)]
passw=''.join(ra)
window=Tk()
window.title("username and password")
usernamei=Button(window,text="Username=>").grid(row=0,column=0)
usernamef=Button(window,text=a[0]).grid(row=0,column=1)
passwordi=Button(window,text="Password=>").grid(row=1,column=0)
passwordf=Button(window,text=passw).grid(row=1,column=1)
f=open("temp1.txt","a+")
f.write(passw)
f.close()
os.system("encryptpasswd.py")
Button(window,text="OK",command=quit).grid(row=2,column=0)
window.mainloop()

