from math import sqrt
import math
from itertools import combinations 
import sqlite3

num_of_student=40
num_of_topic=6

def get_data_according_id():
    con = sqlite3.connect('Students.db')
    cur=con.cursor()
    data =[]
    for i in range(1,num_of_student+1):
        temp=[]
        for j in range(1,num_of_topic+1):
            cur.execute('Select * From Grade where student_id='+str(i) + ' AND topic_id='+str(j))
            r = cur.fetchall()
            temp.append(r[0][2])
        data.append(temp)
    con.close()
    return data

def manhattan(a, b):
    return sum(abs(val1-val2) for val1, val2 in zip(a,b))


my_sum =0 
data=get_data_according_id()


i=0
comb = combinations([i,i+1,i+2,i+3,i+4,i+5,i+6,i+7,i+8,i+9,i+10,i+11,i+12,i+13,i+14,i+15,i+16,i+17,i+18,i+19,i+20,i+21,i+22,i+23,i+24,i+25,i+26,i+27,i+28,i+29,i+30,i+31,i+32,i+33,i+34,i+35,i+36,i+37,i+38,i+39], 2)  
all_comb = list(comb)
print(all_comb)
for c in all_comb:
    my_sum =my_sum +manhattan(data[c[0]],data[c[1]])




print('\n\nThe sum of Manhattan distance for 2 students chosen from 40 students ')
print(my_sum)

def dist():
    c= math.comb(num_of_student,2)
    divi=c/6
    
    return my_sum/divi