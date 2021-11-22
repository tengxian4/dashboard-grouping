import sqlite3
con =sqlite3.connect('Students.db')
cur =con.cursor()
cur.execute('Select * From Question')
 
r = cur.fetchall() 
for i in range(60):
    if r[i][6]=='A':
        print("{\n"+"title: \'"+r[i][1] +"\',\n"+"choices: [\'"+r[i][2]+"\', \'"+r[i][3]+"\',\'"+r[i][4]+"\',\'"+r[i][5]+"\'],\n" +"answer: \'"+r[i][2]+"\',\n" + "topic_id: "+str(r[i][7])+"\n},")
    elif r[i][6]=='B':
        print("{\n"+"title: \'"+r[i][1] +"\',\n"+"choices: [\'"+r[i][2]+"\', \'"+r[i][3]+"\',\'"+r[i][4]+"\',\'"+r[i][5]+"\'],\n" +"answer: \'"+r[i][3]+"\',\n" + "topic_id: "+str(r[i][7])+"\n},")
    elif r[i][6]=='C':
        print("{\n"+"title: \'"+r[i][1] +"\',\n"+"choices: [\'"+r[i][2]+"\', \'"+r[i][3]+"\',\'"+r[i][4]+"\',\'"+r[i][5]+"\'],\n" +"answer: \'"+r[i][4]+"\',\n" + "topic_id: "+str(r[i][7])+"\n},")
    elif r[i][6]=='D':
        print("{\n"+"title: \'"+r[i][1] +"\',\n"+"choices: [\'"+r[i][2]+"\', \'"+r[i][3]+"\',\'"+r[i][4]+"\',\'"+r[i][5]+"\'],\n" +"answer: \'"+r[i][5]+"\',\n" + "topic_id: "+str(r[i][7])+"\n},")


con.close()
 