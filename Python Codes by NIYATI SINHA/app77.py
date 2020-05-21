#Generating Random Values
import random
for i in range(3): #range is an object
    print(random.random())
#for i in range(3): #range is an object
#    print(random.randint()) #error without arguments #TypeError: randint() missing 2 required positional arguments: 'a' and 'b'
for i in range(3): #range is an object
    print(random.randint(2,9))
#for i in range(3): #range is an object
#    print(random.random(1,2))# error #TypeError: random() takes no arguments (2 given)
#Run Again