filepath = 'temp.txt'
    a=[]
    with open(filepath) as fp:  
        line = fp.readline()
        cnt = 1
    
        while line:
            a.append(line.strip())
            line = fp.readline()
            cnt += 1
    c.execute("INSERT INTO stuffToPlot (FirstName,MiddleName,LastName,Age,Sex,Date_of_Birth,Gmail,Phone_Number,User_name,Password)VALUES(?,?,?,?,?,?,?,?,?)",(a[0],a[1],a[2],a[3],a[4],a[5],a[6],a[7],a[0],a[8]))
    conn.commit()
    c.close()
    conn.close()
