import sqlite3
import random
import names

con = sqlite3.connect('Students.db')
cur = con.cursor()
# Create table
cur.execute('''CREATE TABLE Student
               (Id integer primary key, Name varchar,Password varchar)''')


cur.execute('''CREATE TABLE Topic(Id integer primary key,Name varchar)''')
				
cur.execute('''CREATE TABLE Grade
				(Student_Id integer,Topic_Id integer, Result integer,PRIMARY KEY(Student_Id,Topic_Id), FOREIGN KEY(Student_Id) REFERENCES Student(Id), FOREIGN KEY(Topic_Id) REFERENCES Topic(Id))''')


cur.execute('''CREATE TABLE Progress
                                (Id integer primary key,Score1 integer,  Score2 integer,Score3 integer,
                               Score4 integer, Score5 integer, Score6 integer, Student_Id integer,Foreign Key(Student_id) REFERENCES Student(Id))''')
	
cur.execute('''CREATE TABLE Question
               (Id integer, Question varchar,
                Selection_A varchar,
                Selection_B varchar,
                Selection_C varchar,
                Selection_D varchar,
                Answer char,
                Topic_Id integer,
                FOREIGN KEY(Topic_Id) REFERENCES Topic(Id))''')

cur.execute('''CREATE TABLE Teacher
				(Id integer primary key, Name varchar, Password varchar)''')

con.commit()
#insert student
#sample
cur.execute("INSERT INTO Student VALUES (1, 'Abu','123')")

for x in range(2,41):
	cur.execute("INSERT INTO Student (Id, Name,Password) values(?,?,?)",(x,names.get_full_name(),'123'))
	x=x+1

#insert Grade
'''for x in range(1,41):
	for y in range(1,11):
		cur.execute("INSERT INTO Grade (Student_Id,Topic_Id,Result) values(?,?,?)",(x,y,random.randint(0,10)))
'''	


cur.execute("""INSERT INTO Topic VALUES(1,'Adjectives and adverbs')""")

cur.execute("""INSERT INTO Question VALUES(1,'We_________to school by bus.'
                                            ,"always go","go always",'-','-','A','1')""")
cur.execute("""INSERT INTO Question VALUES(2,'I_________my room on Saturdays.'
                                            ,"clean often","often clean",'-','-','B','1')""")
cur.execute("""INSERT INTO Question VALUES(3,'They_________tablets in the classroom. '
                                            ,"sometimes use","use sometimes",'-','-','A','1')""")
cur.execute("""INSERT INTO Question VALUES(4,"He_________home before 8 pm."
                                            ,'gets never','never gets','-','-','B','1')""")
cur.execute("""INSERT INTO Question VALUES(5,"They_________ friendly."
                                            ,'always are','are always','-','-','B','1')""")
cur.execute("""INSERT INTO Question VALUES(6,"The children_________YouTube videos."
                                            ,'often watch','watch often','-','-','A','1')""")
cur.execute("""INSERT INTO Question VALUES(7,'I_________my bed.'
                                            ,'make seldom','seldom make','-','-','B','1')""")
cur.execute("""INSERT INTO Question VALUES(8,'Our teacher_________busy.'
                                            ,'is often','often is','-','-','A','1')""")
cur.execute("""INSERT INTO Question VALUES(9,'Do they_________to the supermarket?'
                                            ,'never walk','walk never','-','-','A','1')""")
cur.execute("""INSERT INTO Question VALUES(10,"We don't_________coffee for breakfast."
                                             ,'always have','have always','-','-','A','1')""")


cur.execute("""INSERT INTO Topic VALUES(2,'Articles a, an, the')""")

cur.execute("""INSERT INTO Question VALUES(1,'Their car does 150 miles_________hour.'
                                            ,"a","an",'the','x','B','2')""")
cur.execute("""INSERT INTO Question VALUES(2,"Where's_________USB drive I lent you last week?"
                                            ,"a","an",'the','x','C','2')""")
cur.execute("""INSERT INTO Question VALUES(3,'Do you still live in_________Bristol?'
                                            ,"a","an",'the','x','D','2')""")
cur.execute("""INSERT INTO Question VALUES(4,"Is your mother working in_________old office building?"
                                            ,"a","an",'the','x','B','2')""")
cur.execute("""INSERT INTO Question VALUES(5,"Carol's father works as_________ electrician."
                                            ,"a","an",'the','x','B','2')""")
cur.execute("""INSERT INTO Question VALUES(6,"The tomatoes are 99 pence_________kilo."
                                            ,"a","an",'the','x','A','2')""")
cur.execute("""INSERT INTO Question VALUES(7,'What do you usually have for _________breakfast?'
                                            ,"a","an",'the','x','D','2')""")
cur.execute("""INSERT INTO Question VALUES(8,'Ben has_________terrible headache.'
                                            ,"a","an",'the','x','A','2')""")
cur.execute("""INSERT INTO Question VALUES(9,'After this tour you have________whole afternoon free to explore the city.'
                                            ,"a","an",'the','x','C','2')""")
cur.execute("""INSERT INTO Question VALUES(10,"Look at_________sea!"
                                             ,"a","an",'the','x','C','2')""")


cur.execute("INSERT INTO Topic VALUES(3,'Conditional sentences (if-clauses and main clauses)')")

cur.execute("""INSERT INTO Question VALUES(1,'If we_________to Dresden, it will be a fantastic trip.'
                                            ,"cycle","cycles",'cycled','-','A','3')""")
cur.execute("""INSERT INTO Question VALUES(2,"I_________the school bus if I don't get up early."
                                            ,"will miss","would miss",'-','-','A','3')""")
cur.execute("""INSERT INTO Question VALUES(3,'Harriet would stay longer in Vienna if she_________more time.'
                                            ,"has","had",'-','-','B','3')""")
cur.execute("""INSERT INTO Question VALUES(4,"She_______the people in Peru if she bought her coffee beans in this shop."
                                            ,"will support","would support",'-','-','B','3')""")
cur.execute("""INSERT INTO Question VALUES(5,"If I don't see Claire today, I_________ her this evening."
                                            ,"will phone","would phone",'-','-','A','3')""")
cur.execute("""INSERT INTO Question VALUES(6,"If Carlos_________sailing, he'll need a life-jacket."
                                            ,"go","goes",'would go','-','B','3')""")
cur.execute("""INSERT INTO Question VALUES(7,'If my brother_________his car here,the traffic warden would give him a ticket.'
                                            ,'park','parks','parked','-','C','3')""")
cur.execute("""INSERT INTO Question VALUES(8,"You'll catch a cold if you_________a pullover."
                                            ,"don't wear","doesn't wear","didn't wear",'-','A','3')""")
cur.execute("""INSERT INTO Question VALUES(9,'If you drink more of this sweet lemonade, you_________sick.'
                                            ,'will get','would get','-','-','A','3')""")
cur.execute("""INSERT INTO Question VALUES(10,"If Marcus sings in the shower, I_________the radio up to full volume."
                                             ,"will turn up","would turn up",'-','-','A','3')""")


cur.execute("INSERT INTO Topic VALUES(4,'Endings of nouns and verbs')")
cur.execute("""INSERT INTO Question VALUES(1,'We read books.(books) =_________'
                                            ,"Noun","Verb",'-','-','A','4')""")
cur.execute("""INSERT INTO Question VALUES(2,'She rides a horse.(rides) =_________'
                                            ,"Noun","Verb",'-','-','B','4')""")
cur.execute("""INSERT INTO Question VALUES(3,'My parents are nice.(parents) =_________'
                                            ,"Noun","Verb",'-','-','A','4')""")
cur.execute("""INSERT INTO Question VALUES(4,"They play the drums.(drums)  = _________"
                                            ,'Noun','Verb','-','-','A','4')""")
cur.execute("""INSERT INTO Question VALUES(5,"He often helps his brother.(helps) = _________"
                                            ,'Noun','Verb','-','-','B','4')""")
cur.execute("""INSERT INTO Question VALUES(6,"I like your computer.(like) = _________"
                                            ,'Noun','Verb','-','-','B','4')""")
cur.execute("""INSERT INTO Question VALUES(7,'We live in a small town.(town) =_________'
                                            ,'Noun','Verb','-','-','A','4')""")
cur.execute("""INSERT INTO Question VALUES(8,'They play handball.(play) =_________'
                                          ,'Noun','Verb','-','-','B','4')""")
cur.execute("""INSERT INTO Question VALUES(9,'His friend has a pet.(friend) =_________'
                                            ,'Noun','Verb','-','-','A','4')""")
cur.execute("""INSERT INTO Question VALUES(10,"I go to bed at 9 o'clock.(go) =_________"
                                             ,'Noun','Verb','-','-','B','4')""")


cur.execute("""INSERT INTO Topic VALUES(5,"Plural, 's, one")""")

cur.execute("""INSERT INTO Question VALUES(1,"our teacher 's tablet = _________"
                                            ,"1 teacher and 1 tablet","1 teacher and more tablets"
                                            ,'more teachers and 1 tablet','more teachers and more tablets','A','5')""")
cur.execute("""INSERT INTO Question VALUES(2,"the dogs' hut = _________"
                                            ,"1 dog and 1 hut","1 dogs and more huts"
                                            ,'more dogs and 1 hut','more dogs and more huts ','C','5')""")
cur.execute("""INSERT INTO Question VALUES(3,"the men's sandwiches = _________"
                                            ,"1 man and 1 sandwich","1 man and more sandwiches"
                                            ,'more men and 1 sandwich','more men and more sandwiches','D','5')""")
cur.execute("""INSERT INTO Question VALUES(4,"This bag is very old. I need a new_________"
                                            ,"one","ones",'-','-','A','5')""")
cur.execute("""INSERT INTO Question VALUES(5,"Small pineapples are sweeter than big_________"
                                            ,"one","ones",'-','-','B','5')""")
cur.execute("""INSERT INTO Question VALUES(6,"The new smartphones are much faster than the old _________"
                                            ,"one","ones",'-','-','B','5')""")
cur.execute("""INSERT INTO Question VALUES(7,'If you buy two bottles of water, you get a third_________free.'
                                            ,'one','ones','-','-','A','5')""")
cur.execute("""INSERT INTO Question VALUES(8,"I would like to have a cupcake – the red_________looks great."
                                            ,"one","ones","-",'-','A','5')""")
cur.execute("""INSERT INTO Question VALUES(9,'This is_________ book.'
                                            ,"Julian's","Julians'",'-','-','A','5')""")
cur.execute("""INSERT INTO Question VALUES(10,"He is_________brother."
                                             ,"Laura's","Lauras'",'-','-','A','5')""")


cur.execute("INSERT INTO Topic VALUES(6,'Irregular and regular verbs')")

cur.execute("""INSERT INTO Question VALUES(1,"swear = _________"
                                            ,"Infinitive","Simple Past",'Past Participle','-','A','6')""")
cur.execute("""INSERT INTO Question VALUES(2,"stolen = _________"
                                            ,"Infinitive","Simple Past",'Past Participle','-','C','6')""")
cur.execute("""INSERT INTO Question VALUES(3,"taken = _________"
                                            ,"Infinitive","Simple Past",'Past Participle','-','C','6')""")
cur.execute("""INSERT INTO Question VALUES(4,"sang = _________"
                                            ,"Infinitive","Simple Past",'Past Participle','-','B','6')""")
cur.execute("""INSERT INTO Question VALUES(5,"saw = _________"
                                            ,"Infinitive","Simple Past",'Past Participle','-','B','6')""")
cur.execute("""INSERT INTO Question VALUES(6,"sink = _________"
                                            ,"Infinitive","Simple Past",'Past Participle','-','A','6')""")
cur.execute("""INSERT INTO Question VALUES(7,"eat = _________"
                                            ,"Infinitive","Simple Past",'Past Participle','-','A','6')""")
cur.execute("""INSERT INTO Question VALUES(8,"spoken = _________"
                                            ,"Infinitive","Simple Past",'Past Participle','-','C','6')""")
cur.execute("""INSERT INTO Question VALUES(9,"gone = _________"
                                            ,"Infinitive","Simple Past",'Past Participle','-','C','6')""")
cur.execute("""INSERT INTO Question VALUES(10,"drunk = _________"
                                             ,"Infinitive","Simple Past",'Past Participle','-','C','6')""")

#store number of question per topic
#the id same as progress id
#for counting the grade
cur.execute('''CREATE TABLE numberOfQuestion 
				(Id integer primary key, no_q1 integer, no_q2 integer, no_q3 integer, no_q4 integer, 
				no_q5 integer, no_q6 integer)''')


for i in range(1,41):     
    cur.execute("Insert INTO numberOfQuestion (Id,no_q1,no_q2,no_q3,no_q4,no_q5,no_q6) values(?,?,?,?,?,?,?)",
        (i,3,3,3,3,3,3))


for i in range(1,41):
    cur.execute("INSERT INTO Progress (Id,Score1,Score2,Score3,Score4,Score5,Score6,Student_Id) values(?,?,?,?,?,?,?,?)",(i,random.randint(0,3), random.randint(0,3), random.randint(0,3), random.randint(0,3), random.randint(0,3), random.randint(0,3),i))


for x in range(2):
    for usr_id in range(1,41):
        cur.execute('Select Score1,Score2,Score3,Score4,Score5,Score6 From Progress Where Student_Id='+str(usr_id))
        score =cur.fetchall()

        cur.execute('Select id From Progress')
        progress=cur.fetchall()

        last_progress=progress[-1][0]+1
        
        if score == []:#if the student has not done any exercies before
            cur.execute("Insert INTO numberOfQuestion (Id,no_q1,no_q2,no_q3,no_q4,no_q5,no_q6) values(?,?,?,?,?,?,?)",
                (last_progress,3,3,3,3,3,3))
            cur.execute("INSERT INTO Progress (Id,Score1,Score2,Score3,Score4,Score5,Score6,Student_Id), values(?,?,?,?,?,?,?,?)",(last_progress,
                random.randint(0,3), random.randint(0,3), random.randint(0,3), random.randint(0,3), random.randint(0,3), random.randint(0,3),usr_id))
        elif sum(score[-1])==18:
            cur.execute("Insert INTO numberOfQuestion (Id,no_q1,no_q2,no_q3,no_q4,no_q5,no_q6) values(?,?,?,?,?,?,?)",
                (last_progress,3,3,3,3,3,3))
            cur.execute("INSERT INTO Progress (Id,Score1,Score2,Score3,Score4,Score5,Score6,Student_Id), values(?,?,?,?,?,?,?,?)",(last_progress,
                random.randint(0,3), random.randint(0,3), random.randint(0,3), random.randint(0,3), random.randint(0,3), random.randint(0,3),usr_id))
        elif score !=[]:       #if not empty
            topic = score[-1].index(min(score[-1]))+1   
        
            if topic ==1:
                cur.execute("Insert INTO numberOfQuestion (Id,no_q1,no_q2,no_q3,no_q4,no_q5,no_q6) values(?,?,?,?,?,?,?)",
                (last_progress,9,2,2,2,2,1))
                cur.execute("INSERT INTO Progress (Id,Score1,Score2,Score3,Score4,Score5,Score6,Student_Id) values(?,?,?,?,?,?,?,?)",(last_progress,
                random.randint(0,9), random.randint(0,2), random.randint(0,2), random.randint(0,2), random.randint(0,2), random.randint(0,1),usr_id))
            elif topic ==2:
                cur.execute("Insert INTO numberOfQuestion (Id,no_q1,no_q2,no_q3,no_q4,no_q5,no_q6) values(?,?,?,?,?,?,?)",
                (last_progress,2,9,2,2,2,1))
                cur.execute("INSERT INTO Progress (Id,Score1,Score2,Score3,Score4,Score5,Score6,Student_Id) values(?,?,?,?,?,?,?,?)",(last_progress,
                random.randint(0,2), random.randint(0,9), random.randint(0,2), random.randint(0,2), random.randint(0,2), random.randint(0,1),usr_id))
            elif topic ==3:
                cur.execute("Insert INTO numberOfQuestion (Id,no_q1,no_q2,no_q3,no_q4,no_q5,no_q6) values(?,?,?,?,?,?,?)",
                (last_progress,2,2,9,2,2,1))
                cur.execute("INSERT INTO Progress (Id,Score1,Score2,Score3,Score4,Score5,Score6,Student_Id) values(?,?,?,?,?,?,?,?)",(last_progress,
                random.randint(0,2), random.randint(0,2), random.randint(0,9), random.randint(0,2), random.randint(0,2), random.randint(0,1),usr_id))
            elif topic ==4:
                cur.execute("Insert INTO numberOfQuestion (Id,no_q1,no_q2,no_q3,no_q4,no_q5,no_q6) values(?,?,?,?,?,?,?)",
                (last_progress,2,2,2,9,2,1))
                cur.execute("INSERT INTO Progress (Id,Score1,Score2,Score3,Score4,Score5,Score6,Student_Id) values(?,?,?,?,?,?,?,?)",(last_progress,
                random.randint(0,2), random.randint(0,2), random.randint(0,2), random.randint(0,9), random.randint(0,2), random.randint(0,1),usr_id))
            elif topic ==5:
                cur.execute("Insert INTO numberOfQuestion (Id,no_q1,no_q2,no_q3,no_q4,no_q5,no_q6) values(?,?,?,?,?,?,?)",
                (last_progress,2,2,2,2,9,1))
                cur.execute("INSERT INTO Progress (Id,Score1,Score2,Score3,Score4,Score5,Score6,Student_Id) values(?,?,?,?,?,?,?,?)",(last_progress,
                random.randint(0,2), random.randint(0,2), random.randint(0,2), random.randint(0,2), random.randint(0,9), random.randint(0,1),usr_id))
            elif topic ==6:
                cur.execute("Insert INTO numberOfQuestion (Id,no_q1,no_q2,no_q3,no_q4,no_q5,no_q6) values(?,?,?,?,?,?,?)",
                (last_progress,2,2,2,2,1,9))
                cur.execute("INSERT INTO Progress (Id,Score1,Score2,Score3,Score4,Score5,Score6,Student_Id) values(?,?,?,?,?,?,?,?)",(last_progress,
                random.randint(0,2), random.randint(0,2), random.randint(0,2), random.randint(0,2), random.randint(0,1), random.randint(0,9),usr_id))


last_score=[]
secondLast_score=[]
thirdLast_score =[]

for id in range(1,41):
    cur.execute('Select id, score1,score2,score3,score4,score5,score6,Student_id From Progress Where Student_Id='+str(id))
    r=cur.fetchall()
    last_score.append(r[-1])
    secondLast_score.append(r[-2])
    thirdLast_score.append(r[-3])



last_no_question=[]
secondLast_no_question=[]
thirdLast_no_question=[]


for id in range(1,41):
    cur.execute('Select no_q1,no_q2,no_q3,no_q4,no_q5,no_q6 From numberOfQuestion Where id='+str(last_score[id-1][0]))
    last_no_question=cur.fetchall()
    
    cur.execute('Select no_q1,no_q2,no_q3,no_q4,no_q5,no_q6 From numberOfQuestion Where id='+str(secondLast_score[id-1][0]))
    secondLast_no_question = cur.fetchall()
    
    cur.execute('Select no_q1,no_q2,no_q3,no_q4,no_q5,no_q6 From numberOfQuestion Where id='+str(thirdLast_score[id-1][0]))
    thirdLast_no_question=cur.fetchall()
    student_grade=[]
    for i in range(1,7):
        student_grade.append(round((((last_score[id-1][i]+secondLast_score[id-1][i]+thirdLast_score[id-1][i])/(last_no_question[0][i-1]+secondLast_no_question[0][i-1]+thirdLast_no_question[0][i-1]))*10)))
    
    for i in range(1,7):
        cur.execute('Select * From Grade Where Student_id='+str(id)+ ' AND Topic_id=' + str(i))
        grades=cur.fetchall() 
        if grades ==[]:
            cur.execute('INSERT INTO Grade (Student_Id,Topic_Id,Result) values(?,?,?)',(id, i,student_grade[i-1]))
        else:
            cur.execute("Update Grade SET Result="+str(student_grade[i-1])+" Where Student_Id="+str(id) +" AND Topic_id="+str(i))
            

con.commit()
con.close()

