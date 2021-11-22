import random
from pyeasyga import pyeasyga
import numpy 
import math
from itertools import combinations 



num_of_student = 40
num_of_topic =10
num_of_person_each_group = 4
num_of_group = math.ceil(num_of_student/num_of_person_each_group) 

    # initialise the GA
def run():
    

    x=0
    seed_data =[]
    for x in range(num_of_student):
        seed_data.append(int(x/num_of_person_each_group))
        x=x+1

    ga = pyeasyga.GeneticAlgorithm(seed_data,
                                population_size=100,
                                generations=50,
                                crossover_probability=0.8,
                                mutation_probability=0.2,
                                elitism=True,
                                maximise_fitness=True)

    ga.create_individual = create_individual
    ga.crossover_function = crossover
    ga.mutate_function = mutate
    ga.selection_function = selection

    ga.fitness_function = fitness       # set the GA's fitness function
    ga.run()

    if ga.best_individual()[0]:
        print (ga.best_individual())
        group_list = ga.best_individual()[1]
        return group_list
    else:
        print (None)

def get_data():
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
        

    

                           