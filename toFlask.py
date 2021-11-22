from flask import Flask, redirect,url_for,render_template, request
from flask import g


import Grouping_GA
import sqlite3
import numpy
import json
import random


DATABASE = './students.db'

TOTAL_TOPIC=[1,2,3,4,5,6]

app =Flask(__name__)

@app.route("/")
def home():
	return"Hello, my main page."


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

def insert_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    r = get_db().commit()
    cur.close()
    return r

@app.route("/displayGA")
def GA():
    student_name = query_db('Select name From Student')
    group_list=Grouping_GA.run()
    '''grouping =zip(group_list,student_name)
    a =tuple(grouping)
    print(group_list)'''



    return render_template("grouping.html",student_name= student_name, group_list=group_list)
    #return "jello"

@app.route("/result")
def result():
   
    topic_names=()
    student_grades=[]
    students_id = query_db('SELECT id FROM Student')
    result_topic=[]
    for id in TOTAL_TOPIC:
        grades=()
        for student in students_id:
            #find the result for each topic and for each student
            # students_id is [(1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,),......]
            grade = query_db('SELECT result FROM Grade WHERE Topic_id='+str(id) +' AND Student_id='+str(student[0]))
            grades=grades+grade[0]
        student_name = query_db('SELECT name FROM Student')
        #array of tuple(student_name, grade), result_topic[0] is the student name and grade for the first topic
        result_topic.append(zip(student_name,grades))
        student_grades.append(grades)

        topic_name =query_db('SELECT name FROM Topic WHERE id='+str(id))
        topic_names=topic_names+ topic_name[0]


    return render_template("tables.html",student_name= student_name, grades=student_grades,topic_names=topic_names)


@app.route("/dashboard")
def dashboard():
    topic_names=()
    student_grades=[]
    students_id = query_db('SELECT id FROM Student')
    result_topic=[]
    for id in TOTAL_TOPIC:
        grades=()
        for student in students_id:
            #find the result for each topic and for each student
            # students_id is [(1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,),......]
            grade = query_db('SELECT result FROM Grade WHERE Topic_id='+str(id) +' AND Student_id='+str(student[0]))
            grades=grades+grade[0]
        student_name = query_db('SELECT name FROM Student')
        #array of tuple(student_name, grade), result_topic[0] is the student name and grade for the first topic
        result_topic.append(zip(student_name,grades))
        student_grades.append(grades)

        topic_name =query_db('SELECT name FROM Topic WHERE id='+str(id))
        topic_names=topic_names+ topic_name[0]



    for rr in result_topic:
        #print(tuple(rr))
        a= list(tuple(rr))
        print("a is ")
        for i in range(0,40):
            print(a[i])
    ''' b=[]
    for rr in result_topic:
        a= numpy.asarray(list(tuple(rr)))
        b.append(a)
    print(b)'''
    print("topic names")
    print(topic_names)
    
    grades=[]
    for g in student_grades:
        grades.append(list(g))
    print(grades)

    frequency1=[0,0,0,0,0,0,0,0,0,0,0]
    for g in grades[0]:
        if g==0:
            frequency1[0]=frequency1[0]+1
        elif g==1:
            frequency1[1]=frequency1[1]+1
        elif g==2:
            frequency1[2]=frequency1[2]+1
        elif g==3:
            frequency1[3]=frequency1[3]+1
        elif g==4:
            frequency1[4]=frequency1[4]+1
        elif g==5:
            frequency1[5]=frequency1[5]+1
        elif g==6:
            frequency1[6]=frequency1[6]+1
        elif g==7:
            frequency1[7]=frequency1[7]+1
        elif g==8:
            frequency1[8]=frequency1[8]+1
        elif g==9:
            frequency1[9]=frequency1[9]+1
        elif  g==10:
            frequency1[10]=frequency1[10]+1   

    print(frequency1)
    #frequency1 for topic 1

    frequency2=[0,0,0,0,0,0,0,0,0,0,0]
    for g in grades[1]:
        if g==0:
            frequency2[0]=frequency2[0]+1
        elif g==1:
            frequency2[1]=frequency2[1]+1
        elif g==2:
            frequency2[2]=frequency2[2]+1
        elif g==3:
            frequency2[3]=frequency2[3]+1
        elif g==4:
            frequency2[4]=frequency2[4]+1
        elif g==5:
            frequency2[5]=frequency2[5]+1
        elif g==6:
            frequency2[6]=frequency2[6]+1
        elif g==7:
            frequency2[7]=frequency2[7]+1
        elif g==8:
            frequency2[8]=frequency2[8]+1
        elif g==9:
            frequency2[9]=frequency2[9]+1
        elif  g==10:
            frequency2[10]=frequency2[10]+1  


    frequency3=[0,0,0,0,0,0,0,0,0,0,0]
    for g in grades[2]:
        if g==0:
            frequency3[0]=frequency3[0]+1
        elif g==1:
            frequency3[1]=frequency3[1]+1
        elif g==2:
            frequency3[2]=frequency3[2]+1
        elif g==3:
            frequency3[3]=frequency3[3]+1
        elif g==4:
            frequency3[4]=frequency3[4]+1
        elif g==5:
            frequency3[5]=frequency3[5]+1
        elif g==6:
            frequency3[6]=frequency3[6]+1
        elif g==7:
            frequency3[7]=frequency3[7]+1
        elif g==8:
            frequency3[8]=frequency3[8]+1
        elif g==9:
            frequency3[9]=frequency3[9]+1
        elif  g==10:
            frequency3[10]=frequency3[10]+1 


    frequency4=[0,0,0,0,0,0,0,0,0,0,0]
    for g in grades[3]:
        if g==0:
            frequency4[0]=frequency4[0]+1
        elif g==1:
            frequency4[1]=frequency4[1]+1
        elif g==2:
            frequency4[2]=frequency4[2]+1
        elif g==3:
            frequency4[3]=frequency4[3]+1
        elif g==4:
            frequency4[4]=frequency4[4]+1
        elif g==5:
            frequency4[5]=frequency4[5]+1
        elif g==6:
            frequency4[6]=frequency4[6]+1
        elif g==7:
            frequency4[7]=frequency4[7]+1
        elif g==8:
            frequency4[8]=frequency4[8]+1
        elif g==9:
            frequency4[9]=frequency4[9]+1
        elif  g==10:
            frequency4[10]=frequency4[10]+1 


    frequency5=[0,0,0,0,0,0,0,0,0,0,0]
    for g in grades[4]:
        if g==0:
            frequency5[0]=frequency5[0]+1
        elif g==1:
            frequency5[1]=frequency5[1]+1
        elif g==2:
            frequency5[2]=frequency5[2]+1
        elif g==3:
            frequency5[3]=frequency5[3]+1
        elif g==4:
            frequency5[4]=frequency5[4]+1
        elif g==5:
            frequency5[5]=frequency5[5]+1
        elif g==6:
            frequency5[6]=frequency5[6]+1
        elif g==7:
            frequency5[7]=frequency5[7]+1
        elif g==8:
            frequency5[8]=frequency5[8]+1
        elif g==9:
            frequency5[9]=frequency5[9]+1
        elif  g==10:
            frequency5[10]=frequency5[10]+1 


    frequency6=[0,0,0,0,0,0,0,0,0,0,0]
    for g in grades[5]:
        if g==0:
            frequency6[0]=frequency6[0]+1
        elif g==1:
            frequency6[1]=frequency6[1]+1
        elif g==2:
            frequency6[2]=frequency6[2]+1
        elif g==3:
            frequency6[3]=frequency6[3]+1
        elif g==4:
            frequency6[4]=frequency6[4]+1
        elif g==5:
            frequency6[5]=frequency6[5]+1
        elif g==6:
            frequency6[6]=frequency6[6]+1
        elif g==7:
            frequency6[7]=frequency6[7]+1
        elif g==8:
            frequency6[8]=frequency6[8]+1
        elif g==9:
            frequency6[9]=frequency6[9]+1
        elif  g==10:
            frequency6[10]=frequency6[10]+1 

    return render_template("dashboard.html",student_name= student_name, grades=grades,topic_names=topic_names,
    frequency1=frequency1,frequency2=frequency2,frequency3=frequency3,frequency4=frequency4,frequency5=frequency5,
    frequency6=frequency6)


@app.route("/quiz")#,method=['POST','GET']
def quiz():
    '''if request.method =="POST":
        pattern_questions=request.form["asd"]
    else:'''
    if request.method=='POST':
        print("asd")
        jsdata = request.form['javascript_data']
        print(jsdata)
        
    
    usr_id=request.args.get('user_id',False) #it is better to use this then usr_id=request.args['user_id']
    usr_name=request.args.get('user_name',False)

    score =query_db('Select Score1,Score2,Score3,Score4,Score5,Score6 From Progress Where Student_Id='+str(usr_id))
    not_need_do_quiz=False
    progress=query_db('Select id From Progress')
   
    last_progress=progress[-1][0]


    if score == []:#if the student has not done any exercies before
        for i in range(18):
                personalizedIndex = (random.sample(range(10),3)+random.sample(range(10,20),3)
                +random.sample(range(20,30),3)+random.sample(range(30,40),3)+random.sample(range(40,50),3)+
                random.sample(range(50,60),3))
        insert_db("Insert INTO numberOfQuestion (Id,no_q1,no_q2,no_q3,no_q4,no_q5,no_q6) values(?,?,?,?,?,?,?)",
            (last_progress,3,3,3,3,3,3))
    elif sum(score[-1])==18:
        not_need_do_quiz=True
        print(not_need_do_quiz)
        for i in range(18):
                personalizedIndex = (random.sample(range(10),3)+random.sample(range(10,20),3)
                +random.sample(range(20,30),3)+random.sample(range(30,40),3)+random.sample(range(40,50),3)+
                random.sample(range(50,60),3))
        insert_db("Insert INTO numberOfQuestion (Id,no_q1,no_q2,no_q3,no_q4,no_q5,no_q6) values(?,?,?,?,?,?,?)",
            (last_progress,3,3,3,3,3,3))
    elif score !=[]:       #if not empty
        topic = score[-1].index(min(score[-1]))+1   
    
        if topic ==1:
            for i in range(18):
                personalizedIndex = (random.sample(range(10),9)+random.sample(range(10,20),2)
                +random.sample(range(20,30),2)+random.sample(range(30,40),2)+random.sample(range(40,50),2)+
                random.sample(range(50,60),1)) #not inclusive the greater part, 9 questions for topic 1
            insert_db("Insert INTO numberOfQuestion (Id,no_q1,no_q2,no_q3,no_q4,no_q5,no_q6) values(?,?,?,?,?,?,?)",
            (last_progress,9,2,2,2,2,1))
        elif topic ==2:
            for i in range(18):
                personalizedIndex = (random.sample(range(10),2)+random.sample(range(10,20),9)
                +random.sample(range(20,30),2)+random.sample(range(30,40),2)+random.sample(range(40,50),2)+
                random.sample(range(50,60),1))
            insert_db("Insert INTO numberOfQuestion (Id,no_q1,no_q2,no_q3,no_q4,no_q5,no_q6) values(?,?,?,?,?,?,?)",
            (last_progress,2,9,2,2,2,1))
        elif topic ==3:
            for i in range(18):
                personalizedIndex = (random.sample(range(10),2)+random.sample(range(10,20),2)
                +random.sample(range(20,30),9)+random.sample(range(30,40),2)+random.sample(range(40,50),2)+
                random.sample(range(50,60),1))
            insert_db("Insert INTO numberOfQuestion (Id,no_q1,no_q2,no_q3,no_q4,no_q5,no_q6) values(?,?,?,?,?,?,?)",
            (last_progress,2,2,9,2,2,1))
        elif topic ==4:
            for i in range(18):
                personalizedIndex = (random.sample(range(10),2)+random.sample(range(10,20),2)
                +random.sample(range(20,30),2)+random.sample(range(30,40),9)+random.sample(range(40,50),2)+
                random.sample(range(50,60),1))
            insert_db("Insert INTO numberOfQuestion (Id,no_q1,no_q2,no_q3,no_q4,no_q5,no_q6) values(?,?,?,?,?,?,?)",
            (last_progress,2,2,2,9,2,1))
        elif topic ==5:
            for i in range(18):
                personalizedIndex = (random.sample(range(10),2)+random.sample(range(10,20),2)
                +random.sample(range(20,30),2)+random.sample(range(30,40),2)+random.sample(range(40,50),9)+
                random.sample(range(50,60),1))
            insert_db("Insert INTO numberOfQuestion (Id,no_q1,no_q2,no_q3,no_q4,no_q5,no_q6) values(?,?,?,?,?,?,?)",
            (last_progress,2,2,2,2,9,1))
        elif topic ==6:
            for i in range(18):
                personalizedIndex = (random.sample(range(10),2)+random.sample(range(10,20),2)
                +random.sample(range(20,30),2)+random.sample(range(30,40),2)+random.sample(range(40,50),1)+
                random.sample(range(50,60),9))
            insert_db("Insert INTO numberOfQuestion (Id,no_q1,no_q2,no_q3,no_q4,no_q5,no_q6) values(?,?,?,?,?,?,?)",
            (last_progress,2,2,2,2,1,9))



    return render_template("quiz.html",usr_id=usr_id,usr_name=usr_name,personalizedIndex=personalizedIndex,not_need_do_quiz=not_need_do_quiz )





@app.route('/func', methods=['GET','POST'])
def func():

    score1=0
    score2=0
    score3=0
    score4=0
    score5=0
    score6=0

    dataGet = '' if not request.get_json(force=True) else request.get_json(force=True)
    print(dataGet)
    print(dataGet['page_data'])
    pattern_questions=dataGet['page_data']
    for p in pattern_questions:
        if p==1:
            score1=score1+1
        elif p==2:
            score2=score2+1
        elif p==3:
            score3=score3+1
        elif p==4:
            score4=score4+1
        elif p==5:
            score5=score5+1
        elif p ==6:
            score6=score6+1


    
    print(score1)
    print(score2)
    print(score3)
    print(score4)
    print(score5)
    print(score6)
    r= query_db('Select id FROM Progress')
    progress_id = r[-1][0]+1
    print("progress id is ")
    print(progress_id)
    user_id=dataGet['user_id']
    print(user_id)
    insert_db("INSERT INTO Progress (Id, Score1,Score2,Score3,Score4,Score5,Score6,Student_Id) values(?,?,?,?,?,?,?,?)",(progress_id,score1,score2,score3,score4,score5,score6,user_id))
    
    dataReply = {'backend_data':'some_data'}
    
    return "Success"

def updateGrade():
    totalStudents=len(query_db('Select * From Students'))

    for id in range(totalStudents):
        score= query_db('Select Score1,Score2,Score3,Score4,Score5,Score6,Student_Id From Progress where Student_id='+str(id))
        #questions =query_db(''
        #grade=[]
        number_of_questions=[]
        for i in range(6):
            grade[i] =score[-1][i] +  score[-2][i]+score[-3][i]
        

    return 0



@app.route("/login",methods =['POST','GET'])
def login():
    if request.method=='POST':
        id = request.form['username']
        password=request.form['password']
        user=query_db('Select * From Student Where id='+str(id)+' AND password='+str(password))
        user_id=user[0][0]
        user_name=user[0][1]
        
        return redirect(url_for("quiz",user_id=id,user_name=user_name))
    else:    
        return render_template("login.html")



if __name__=="__main__":
	app.run(debug=True)