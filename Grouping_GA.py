import random
from pyeasyga import pyeasyga
import numpy 
import math
from itertools import combinations 
import sqlite3


not_finish_exercise_student=[]

num_of_student = 40
num_of_topic =6
num_of_person_each_group = 4
num_of_group = math.ceil(num_of_student/num_of_person_each_group) 

    # initialise the GA
def run():
    

    x=0
    seed_data =[]
    for x in range(num_of_student-len(not_finish_exercise_student)):
        seed_data.append(int(x/num_of_person_each_group))
        x=x+1

    ga = pyeasyga.GeneticAlgorithm(seed_data,
                                population_size=20,
                                generations=10,
                                crossover_probability=0.8,
                                mutation_probability=0.01,
                                maximise_fitness=True)#elitism=True,

    ga.create_individual = create_individual
    ga.crossover_function = crossover
    ga.mutate_function = mutate
    ga.selection_function = selection #default selection is tournament

    ga.fitness_function = fitness       # set the GA's fitness function
    ga.run()

    if ga.best_individual()[0]:
        print("\n\nthe sum of Manhattan distance for 2 students chosen from 4 students for each group")
        
        print (ga.best_individual()[0])
        print("\n\n")
        
        print (ga.best_individual())
        group_list = ga.best_individual()[1]
        if len(not_finish_exercise_student)!=0:
            return group_list, ga.best_individual()[0],not_finish_exercise_student
        return group_list, ga.best_individual()[0]
    else:
        print (None)

def get_data():
    con = sqlite3.connect('Students.db')
    cur=con.cursor()
    data =[]
    global not_finish_exercise_student
    not_finish_exercise_student=[]
    for i in range(1,num_of_student+1):
        temp=[]
        for j in range(1,num_of_topic+1):
            cur.execute('Select * From Grade where student_id='+str(i) + ' AND topic_id='+str(j))
            r = cur.fetchall()
            if len(r)==0:
                not_finish_exercise_student.append(i)
            temp.append(r[0][2])
        data.append(temp)
    con.close()
    return data



def get_data_random():
    x=0
    y=0
    data =[]
    for x in range(40): #40 students
        temp=(random.randint(0, 10),)
        for y in range(9): #10 questions
            temp = temp+ (random.randint(0, 10),)
            y=y+1
        data.append(temp)
        x=x+1
    return data

    # define and set function to create a candidate solution representation
def create_individual(data):
    individual = data[:]
    random.shuffle(individual)
    return individual




    # define and set the GA's crossover operation
def crossover(parent_1, parent_2):
    crossover_index = random.randrange(1, len(parent_1))
    child_1a = parent_1[:crossover_index]
    child_1b = [i for i in parent_2 if i not in child_1a]
    child_1 = child_1a + child_1b

    child_2a = parent_2[crossover_index:]
    child_2b = [i for i in parent_1 if i not in child_2a]
    child_2 = child_2a + child_2b

    
    return child_1, child_2




# define and set the GA's mutation operation
def mutate(individual):
    mutate_index1 = random.randrange(len(individual))
    mutate_index2 = random.randrange(len(individual))
    index_val1 = individual[mutate_index1]
    index_val2 = individual[mutate_index2]
    index_val1, index_val2 = index_val2, index_val1




# define and set the GA's selection operation
def selection(population):
    return random.choice(population)





# define a fitness function
def fitness(individual, data):
    data = get_data()
    for x in range(num_of_group): #check whether each has maximum of 4 ppl, if more than 4 ppl then will return 0
        each_group =0
        for ind in individual:
            if ind ==x:
                each_group = each_group+1
                if each_group > 4:
                    return 0
    sum_of_all_diff=0
    for x in range(num_of_group):
        student_index=[]
        sum_diff_each_group=0
        temp_individual = individual.copy()
        for item in temp_individual:
            if item ==x:
                student_index.append(temp_individual.index(item))
                temp_individual[temp_individual.index(item)] = 'A' #so that it will not be detected next time
        
    # Get all combinations of number of student_index
    # and length 2
        comb = combinations(student_index, 2)
        all_comb = list(comb)
        for each_pair in all_comb:
            differents = abs(numpy.subtract(numpy.array(data[each_pair[0]]),numpy.array(data[each_pair[1]])))
            sum_diff_each_group = sum_diff_each_group +sum(differents )
        
        sum_of_all_diff = sum_of_all_diff +sum_diff_each_group 
    return sum_of_all_diff
        

    

                           