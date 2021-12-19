import sqlite3



def get_data(student_id):

    con = sqlite3.connect('Students.db')
    cur = con.cursor()

    cur.execute('SELECT * FROM Progress Where Student_id ='+str(student_id)+ ' ORDER BY ID DESC LIMIT 3')
    r = cur.fetchall()
    
    # get number of question
    all_progress=[]
    for i in range(3):
        progress=[]
        progress.append(r[i][1])
        progress.append(r[i][2])
        progress.append(r[i][3])
        progress.append(r[i][4])
        progress.append(r[i][5])
        progress.append(r[i][6])
        all_progress.append(progress)

   
    question_id=[]
    for i in range(3):
        question_id.append(r[i][0])
    
    no_question3 = get_number_question(question_id[0])
    no_question2=get_number_question(question_id[1])
    no_question1 =get_number_question(question_id[2])

    con.close()
    return all_progress,no_question3,no_question2,no_question1
    


def get_progress(student_id):
    all_progress,no_question3,no_question2,no_question1=get_data(student_id)

    no_question=[]
    no_question.append(no_question3)
    no_question.append(no_question2)
    no_question.append(no_question1)

    return all_progress ,no_question

def get_number_question(question_id):
    
    con = sqlite3.connect('Students.db')
    cur = con.cursor()
    print('In getting the number of question')
    print(question_id)
    cur.execute('SELECT * FROM numberOfQuestion Where id='+str(question_id))
    r = cur.fetchall()
    no_question =[]
    print(r)
    for i in range(6):
        no_question.append(r[0][i+1])

    con.close()
    return no_question