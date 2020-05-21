import random
dice=[1,2,3,4,5,6]
list=[]
#list.append(random.choice,random.choice) #TypeError: append() takes exactly one argument (2 given)
list.append(random.choice(dice))
list.append(random.choice(dice))
print(list)