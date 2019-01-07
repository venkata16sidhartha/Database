##create an encryption
import numpy as np
import random
from tkinter import *
import tkinter as tk
import time
def varf():
    
    var=['q','w','e','r','t','y','u','F','i','o','p','C','D','E','G','l','k','j','h','g','f','d','s','a','z','x','c','v','b','n','m','A','1','2','3','M','N','4','5','6','B','7','8','9','H','I','J','0','!','@','$','%','^','K','L','&','*','(',')','O','P','-','=','+','"','Q','R','S',"'",':','T','U',';',',','<','>','V','W','X','.','/','?','Y','Z','`','~']
    b=random.randint(1,15)
    a=random.randint(b,25)
    pswd=[]
    for j in range(a):
         pswd.append(var[random.randint(1,len(var))-1])
    return pswd    
var=['q','w','e','r','t','y','u','F','i','o','p','C','D','E','G','l','k','j','h','g','f','d','s','a','z','x','c','v','b','n','m','A','1','2','3','M','N','4','5','6','B','7','8','9','H','I','J','0','!','@','$','%','^','K','L','&','*','(',')','O','P','-','=','+','"','Q','R','S',"'",':','T','U',';',',','<','>','V','W','X','.','/','?','Y','Z','`','~']     
enc=[]

def encfn():
    a=''.join(varf())
    if(a not in enc):
        enc.append(a)
    else:
        z=encfn()
for i in range(len(var)):
    z=encfn()      
f=open("enctemp.txt",'w+')
f.write(enc[0])
f.close()
for i in range(1,len(var)):
    f=open("enctemp.txt","a+")
    f.write("\n")
    f.close()
    f=open("enctemp.txt","a+")
    f.write(enc[i])
    f.close()
    
    
