import random

topic =6
if topic ==1:
    for i in range(18):
        personalizedIndex = (random.sample(range(10),9)+random.sample(range(10,20),2)
        +random.sample(range(20,30),2)+random.sample(range(30,40),2)+random.sample(range(40,50),2)+
        random.sample(range(50,60),1)) #not inclusive the greater part, 9 questions for topic 1
elif topic ==2:
    for i in range(18):
        personalizedIndex = (random.sample(range(10),2)+random.sample(range(10,20),9)
        +random.sample(range(20,30),2)+random.sample(range(30,40),2)+random.sample(range(40,50),2)+
        random.sample(range(50,60),1))
elif topic ==3:
    for i in range(18):
        personalizedIndex = (random.sample(range(10),2)+random.sample(range(10,20),2)
        +random.sample(range(20,30),9)+random.sample(range(30,40),2)+random.sample(range(40,50),2)+
        random.sample(range(50,60),1))
elif topic ==4:
    for i in range(18):
        personalizedIndex = (random.sample(range(10),2)+random.sample(range(10,20),2)
        +random.sample(range(20,30),2)+random.sample(range(30,40),9)+random.sample(range(40,50),2)+
        random.sample(range(50,60),1))
elif topic ==5:
    for i in range(18):
        personalizedIndex = (random.sample(range(10),2)+random.sample(range(10,20),2)
        +random.sample(range(20,30),2)+random.sample(range(30,40),2)+random.sample(range(40,50),9)+
        random.sample(range(50,60),1))
elif topic ==6:
    for i in range(18):
        personalizedIndex = (random.sample(range(10),2)+random.sample(range(10,20),2)
        +random.sample(range(20,30),2)+random.sample(range(30,40),2)+random.sample(range(40,50),1)+
        random.sample(range(50,60),9))

print(personalizedIndex)
print(len(personalizedIndex))