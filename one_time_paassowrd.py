import random
from tkinter import *
import time
var=['q','w','e','r','t','y','u','F','i','o','p','C','D','E','G','l','k','j','h','g','f','d','s','a','z','x','c','v','b','n','m','A','1','2','3','M','N','4','5','6','B','7','8','9','H','I','J','0','!','@','$','%','^','K','L','&','*','(',')','O','P','-','=','+','"','Q','R','S',"'",':','T','U',';',',','<','>','V','W','X','.','/','?','Y','Z','`','~']
b=random.randint(1,15)
a=random.randint(b,25)
pswd=[]
for j in range(a):
     pswd.append(var[random.randint(1,len(var))-1]) 
     
root =Tk()
root.title("Click to copy password and exit")
import os

Pswd=''.join(pswd)
Label(root, text=Pswd).grid(row=0,column=0 ,sticky=W) 

slogan =Button(root,
                   text="quit",
		   fg="red",
                   command=quit).grid(row=5,column=1,sticky=W)


root.mainloop()
    
