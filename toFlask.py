from flask import Flask, redirect,url_for,render_template, request,flash
from flask import g
from flask.helpers import flash


import Grouping_GA
import sqlite3
import numpy as np
import json
import random
import performance
import updateDB
import re
import average_distance
import getProgress
import checkDB
import time

DATABASE = './students.db'

TOTAL_TOPIC=[1,2,3,4,5,6]

group_list =[]

student_result_by_group_for_manhattan=0

app =Flask(__name__)
app.secret_key='123456'


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

@app.route("/resultByGroup",methods=['POST','GET'])
def resultByGroup():
    

    # get the performance
    p_name= performance.performance_according_name()
    p_id =performance.performance_according_id()
    overall_dist = average_distance.dist()
    num_group=max(group_list)+1
    overall_dist = int(overall_dist*num_group)

    con =sqlite3.connect('Students.db')
    cur=con.cursor()
    
    dist=request.args.get('dist',False)
    
    
    cur.execute('Select name From Student')
    student_name =cur.fetchall()
    
    #find the member in the same group
    values = np.array(group_list)
    each_group=[]
    
    for i in range(max(group_list)+1):
        each_group.append(np.where(values == i)[0])
        
    
    #get the result for each group
    # the resultByGroup will have student id, student name, score for topic 1-6
    # using 3D array 
    
    all_student_result_by_group =[]
    for eg in each_group:
        resultByGroup=[]
        for i in eg:    
            result_per_student=[]
            result_per_student.append(i+1)
            result_per_student.append(student_name[i][0])
            for t in TOTAL_TOPIC:
                cur.execute('Select result from grade Where student_id='+str(i+1)+" And Topic_id="+str(t))
                r=cur.fetchall()   
                result_per_student.append(r[0][0])
            resultByGroup.append(result_per_student)
            
        all_student_result_by_group.append(resultByGroup)
        global student_result_by_group_for_manhattan
        student_result_by_group_for_manhattan=all_student_result_by_group
    return render_template("resultByGroup.html",all_student_result_by_group=all_student_result_by_group,dist=dist,p_name=p_name,p_id=p_id,overall_dist=overall_dist)



@app.route("/displayGA",methods=['POST','GET'])
def GA():
    
    usr_name=request.args.get('username',False) #it is better to use this then usr_id=request.args['user_id']
    
    if usr_name ==False:
        return redirect(url_for("admin_login"))	

    student_name = query_db('Select name From Student')
    inner_group_list,dist=Grouping_GA.run()
    '''grouping =zip(group_list,student_name)
    a =tuple(grouping)
    print(group_list)'''
    global group_list
    group_list =inner_group_list
    return render_template("grouping.html",student_name= student_name, group_list=inner_group_list,username=usr_name,dist=dist)
    #return "jello"

@app.route("/result",methods=['POST','GET'])
def result():
    
    usr_name=request.args.get('username',False) #it is better to use this then usr_id=request.args['user_id']
    
    if usr_name ==False:
        return redirect(url_for("admin_login"))


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


    return render_template("tables.html",student_name= student_name, grades=student_grades,topic_names=topic_names,username=usr_name)


@app.route("/dashboard",methods=['POST','GET'])
def dashboard():
    
    usr_name=request.args.get('username',False) #it is better to use this then usr_id=request.args['user_id']
    
    if usr_name ==False:
        return redirect(url_for("admin_login"))
    
    updateGrade()
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

    sum1=0
    for g in grades[0]:
        sum1=sum1+g

    sum2=0
    for g in grades[1]:
        sum2=sum2+g

    sum3=0
    for g in grades[2]:
        sum3=sum3+g


    sum4=0
    for g in grades[3]:
        sum4=sum4+g

    sum5=0
    for g in grades[4]:
        sum5=sum5+g

    sum6=0
    for g in grades[5]:
        sum6=sum6+g

    num_of_student=query_db('Select id from Student')
    num_of_student=len(num_of_student)
    avg1 = sum1/num_of_student
    avg2=sum2/num_of_student
    avg3=sum3/num_of_student
    avg4=sum4/num_of_student
    avg5=sum5/num_of_student
    avg6=sum6/num_of_student
   

    return render_template("dashboard.html",student_name= student_name, grades=grades,topic_names=topic_names,avg1=avg1,avg2=avg2,avg3=avg3,avg4=avg4,avg5=avg5,avg6=avg6,username=usr_name)


@app.route("/quiz",methods=['POST','GET'])#,method=['POST','GET']
def quiz():
    
    usr_id=request.args.get('user_id',False) #it is better to use this then usr_id=request.args['user_id']
    usr_name=request.args.get('user_name',False)
    print("user id is ")
    print(usr_id)
    print("user name is ")
    print(usr_name)
    if usr_id ==False or usr_name==False:
        return redirect(url_for("login"))

    score =query_db('Select Score1,Score2,Score3,Score4,Score5,Score6 From Progress Where Student_Id='+str(usr_id))
    not_need_do_quiz=False
    progress=query_db('Select id From Progress')
   
    last_progress=progress[-1][0]+1
    print(last_progress)

    if score == []:#if the student has not done any exercies before
        personalizedIndex = (random.sample(range(10),3)+random.sample(range(10,20),3)
                +random.sample(range(20,30),3)+random.sample(range(30,40),3)+random.sample(range(40,50),3)+
                random.sample(range(50,60),3))
        insert_db("Insert INTO numberOfQuestion (Id,no_q1,no_q2,no_q3,no_q4,no_q5,no_q6) values(?,?,?,?,?,?,?)",
            (last_progress,3,3,3,3,3,3))
        print('Executed [] ')
    elif sum(score[-1])==18:
        not_need_do_quiz=True
        print(not_need_do_quiz)
        personalizedIndex = (random.sample(range(10),3)+random.sample(range(10,20),3)
                +random.sample(range(20,30),3)+random.sample(range(30,40),3)+random.sample(range(40,50),3)+
                random.sample(range(50,60),3))
        insert_db("Insert INTO numberOfQuestion (Id,no_q1,no_q2,no_q3,no_q4,no_q5,no_q6) values(?,?,?,?,?,?,?)",
            (last_progress,3,3,3,3,3,3))
        print("execute sum")
    elif score !=[]:       #if not empty
        topic = score[-1].index(min(score[-1]))+1   
    
        if topic ==1:
            personalizedIndex = (random.sample(range(10),9)+random.sample(range(10,20),2)
                +random.sample(range(20,30),2)+random.sample(range(30,40),2)+random.sample(range(40,50),2)+
                random.sample(range(50,60),1)) #not inclusive the greater part, 9 questions for topic 1
            insert_db("Insert INTO numberOfQuestion (Id,no_q1,no_q2,no_q3,no_q4,no_q5,no_q6) values(?,?,?,?,?,?,?)",
            (last_progress,9,2,2,2,2,1))
            print("execute 1")
        elif topic ==2:
            personalizedIndex = (random.sample(range(10),2)+random.sample(range(10,20),9)
                +random.sample(range(20,30),2)+random.sample(range(30,40),2)+random.sample(range(40,50),2)+
                random.sample(range(50,60),1))
            insert_db("Insert INTO numberOfQuestion (Id,no_q1,no_q2,no_q3,no_q4,no_q5,no_q6) values(?,?,?,?,?,?,?)",
            (last_progress,2,9,2,2,2,1))
            print("execute 2")
        elif topic ==3:
            personalizedIndex = (random.sample(range(10),2)+random.sample(range(10,20),2)
                +random.sample(range(20,30),9)+random.sample(range(30,40),2)+random.sample(range(40,50),2)+
                random.sample(range(50,60),1))
            insert_db("Insert INTO numberOfQuestion (Id,no_q1,no_q2,no_q3,no_q4,no_q5,no_q6) values(?,?,?,?,?,?,?)",
            (last_progress,2,2,9,2,2,1))
            print("execute 3")
        elif topic ==4:
            personalizedIndex = (random.sample(range(10),2)+random.sample(range(10,20),2)
                +random.sample(range(20,30),2)+random.sample(range(30,40),9)+random.sample(range(40,50),2)+
                random.sample(range(50,60),1))
            insert_db("Insert INTO numberOfQuestion (Id,no_q1,no_q2,no_q3,no_q4,no_q5,no_q6) values(?,?,?,?,?,?,?)",
            (last_progress,2,2,2,9,2,1))
            print("execute 4")
        elif topic ==5:
            personalizedIndex = (random.sample(range(10),2)+random.sample(range(10,20),2)
                +random.sample(range(20,30),2)+random.sample(range(30,40),2)+random.sample(range(40,50),9)+
                random.sample(range(50,60),1))
            insert_db("Insert INTO numberOfQuestion (Id,no_q1,no_q2,no_q3,no_q4,no_q5,no_q6) values(?,?,?,?,?,?,?)",
            (last_progress,2,2,2,2,9,1))
            print("execute 5")
        elif topic ==6:
            personalizedIndex = (random.sample(range(10),2)+random.sample(range(10,20),2)
                +random.sample(range(20,30),2)+random.sample(range(30,40),2)+random.sample(range(40,50),1)+
                random.sample(range(50,60),9))
            insert_db("Insert INTO numberOfQuestion (Id,no_q1,no_q2,no_q3,no_q4,no_q5,no_q6) values(?,?,?,?,?,?,?)",
            (last_progress,2,2,2,2,1,9))
            print("execute 5")

    r=query_db('select * from numberofquestion ORDER BY ID DESC LIMIT 1')
    print(r) 
    
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
    time.sleep(2)
    return "Success"# redirect(url_for('login'))

def updateGrade():
    totalStudents=len(query_db('Select * From Student'))
    totalTopic = len(query_db('Select * From Topic'))
    updateDB.update(totalStudents,totalTopic)

    return 0



@app.route("/login",methods =['POST','GET'])
def login():
    time.sleep(2)
    checkDB.check()
    if request.method=='POST':
        id = request.form['username']
        password=request.form['password']
        
        id_int_list=re.findall(r'[^0-9]',id)
        #if the id contain characters or did not enter anything then pop up error msg
        if id_int_list != [] or id=='':
            flash('Looks like you don\'t have an account')
            return redirect(url_for("login"))
        

        try:
            user=query_db('Select * From Student Where id='+str(id)+' AND password='+str(password))
            user_id=user[0][0]
            user_name=user[0][1]
        except IndexError:
            user_id=False

        #if dont have valid account, pop up error msg
        if user_id!=False:
            return redirect(url_for("progress",user_id=id,user_name=user_name))
        else:
            flash('Looks like you don\'t have an account')
            return redirect(url_for("login"))
    else:    
        return render_template("login.html")

@app.route("/admin_login",methods =['POST','GET'])
def admin_login():
    if request.method=='POST':
        username = request.form['username']
        password=request.form['password'] 
     
        if username=='':
            flash('Looks like you don\'t have an account')
            return redirect(url_for("admin_login"))
        

        #if dont have valid account, pop up error msg
        if username=='Admin' and password=='123':
            return redirect(url_for("dashboard",username=username))
        else:
            flash('Looks like you don\'t have an account')
            return redirect(url_for("admin_login"))
    else:    
        return render_template("admin_login.html")


@app.route("/progress",methods =['POST','GET'])
def progress():
    checkDB.check()
    usr_id=request.args.get('user_id',False) #it is better to use this then usr_id=request.args['user_id']
    usr_name=request.args.get('user_name',False)
    
    progress,no_question=getProgress.get_progress(usr_id)
    
    return render_template('progress.html',progress=progress,no_question=no_question,zip=zip,usr_id=usr_id,usr_name=usr_name)

@app.route("/chatbot")
def chatbot():
    return render_template('chatbot.html')

@app.route("/manhattan",methods=['GET'])
def manhattan():
    dist=request.args.get('dist',False) 
    return render_template('manhattan.html',all_student_result_by_group=student_result_by_group_for_manhattan,dist=dist)


@app.route("/test")  
def test():
    return render_template('test.html')  

if __name__=="__main__":
	app.run(debug=True)