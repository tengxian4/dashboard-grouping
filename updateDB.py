import sqlite3



def update(totalStudent, totalTopic):
    last_score=[]
    secondLast_score=[]
    thirdLast_score =[]
    
    con =sqlite3.connect('Students.db')
    cur = con.cursor()

    for id in range(1,totalStudent+1):
        cur.execute('Select id, score1,score2,score3,score4,score5,score6,Student_id From Progress Where Student_Id='+str(id))
        r=cur.fetchall()
        
        

        last_score.append(r[-1])
        secondLast_score.append(r[-2])
        thirdLast_score.append(r[-3])



    last_no_question=[]
    secondLast_no_question=[]
    thirdLast_no_question=[]


    for id in range(1,totalStudent+1):
        cur.execute('Select no_q1,no_q2,no_q3,no_q4,no_q5,no_q6 From numberOfQuestion Where id='+str(last_score[id-1][0]))
        last_no_question=cur.fetchall()
        if len(last_no_question)==0:
            break
        
        cur.execute('Select no_q1,no_q2,no_q3,no_q4,no_q5,no_q6 From numberOfQuestion Where id='+str(secondLast_score[id-1][0]))
        secondLast_no_question = cur.fetchall()
        if len(secondLast_score)==0:
            break

        cur.execute('Select no_q1,no_q2,no_q3,no_q4,no_q5,no_q6 From numberOfQuestion Where id='+str(thirdLast_score[id-1][0]))
        thirdLast_no_question=cur.fetchall()
        student_grade=[]
        for i in range(1,totalTopic+1):
            student_grade.append(round((((last_score[id-1][i]+secondLast_score[id-1][i]+thirdLast_score[id-1][i])/(last_no_question[0][i-1]+secondLast_no_question[0][i-1]+thirdLast_no_question[0][i-1]))*10)))
        
        for i in range(1,totalTopic+1):
            cur.execute('Select * From Grade Where Student_id='+str(id)+ ' AND Topic_id=' + str(i))
            grades=cur.fetchall() 
            if grades ==[]:
                cur.execute('INSERT INTO Grade (Student_Id,Topic_Id,Result) values(?,?,?)',(id, i,student_grade[i-1]))
            else:
                cur.execute("Update Grade SET Result="+str(student_grade[i-1])+" Where Student_Id="+str(id) +" AND Topic_id="+str(i))
                
    con.commit()
    con.close()
