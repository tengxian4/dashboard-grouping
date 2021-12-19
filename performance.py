from math import sqrt
from itertools import combinations 
import sqlite3

num_of_student=40
num_of_topic=6



def get_data_according_name():
    con = sqlite3.connect('Students.db')
    cur=con.cursor()
    data =[]
    cur.execute('Select id FROM student Order By name ASC')
    r = cur.fetchall()
    student_id=[]
    '''cur.execute('Select name from student where id='+str(id))
        r=cur.fetchall()
        print(r)''' #to check the ascending order of the names
    for i in range(1,num_of_student+1):
        student_id.append(r[i-1][0])
    for id in student_id:
        temp=[]
        for j in range(1,num_of_topic+1):
            cur.execute('Select * From Grade where student_id='+str(id) + ' AND topic_id='+str(j))
            r = cur.fetchall()
            temp.append(r[0][2])
        data.append(temp)
    con.close()
    return data
    '''    
    for i in range(1,num_of_student+1):
        temp=[]
        for j in range(1,num_of_topic+1):
            cur.execute('Select * From Grade where student_id='+str(i) + ' AND topic_id='+str(j))
            r = cur.fetchall()
            temp.append(r[0][2])
        data.append(temp)
    con.close()
    return data'''   

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

def performance_according_name():
    my_sum =0 
    data=get_data_according_name()

    for i in range(0,37,4):
        comb = combinations([i,i+1,i+2,i+3], 2)  
        all_comb = list(comb)
        print(all_comb)
        for c in all_comb:
            my_sum =my_sum +manhattan(data[c[0]],data[c[1]])

    print(my_sum)
    return my_sum

def performance_according_id():
    my_sum =0 
    data=get_data_according_id()

    for i in range(0,37,4):
        comb = combinations([i,i+1,i+2,i+3], 2)  
        all_comb = list(comb)
        print(all_comb)
        for c in all_comb:
            my_sum =my_sum +manhattan(data[c[0]],data[c[1]])

    print(my_sum)
    return my_sum