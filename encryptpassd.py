import os
var=['q','w','e','r','t','y','u','F','i','o','p','C','D','E','G','l','k','j','h','g','f','d','s','a','z','x','c','v','b','n','m','A','1','2','3','M','N','4','5','6','B','7','8','9','H','I','J','0','!','@','$','%','^','K','L','&','*','(',')','O','P','-','=','+','"','Q','R','S',"'",':','T','U',';',',','<','>','V','W','X','.','/','?','Y','Z','`','~']
filepath = 'temp1.txt'
a=[]
with open(filepath) as fp:  
    line = fp.readline()
    cnt = 1
    
    while line:
         a.append(line.strip())
         line = fp.readline()
         cnt += 1
z=[]
psd=(a[0])
filepath='enctemp.txt'
with open(filepath) as fp:  
    line = fp.readline()
    cnt = 1
    
    while line:
         z.append(line.strip())
         line = fp.readline()
         cnt += 1
pswf=[]
for i in range(len(psd)):
    for j in range(len(var)):
        if(psd[i]==var[j]):
               pswf.append(z[j])
f=open("temp.txt","a+")
f.write("\n")
f.close()
f=open("temp.txt","a+")
f.write(''.join(pswf))
f.close()
os.remove("temp1.txt")

    
