for item in range(2):#for item in [0,1]
    print(item)#here if we don't give any value in range() error will occur
# range function creates an object, its not a list but its a special kind of object that we can iterate over
# and with each iteration this object spit out a new no
print("_____")
for item in range(2,): # automatically ignores the comma
    print(item)
print("_____")
#for item in range(,5): ERROR WILL OCCUR FOR INVALID SYNTAX
for any_name in range(1,3,):# automatically ignores the comma
    print(any_name)
print("_____")

for any_name in range(2,3,9): #if the jump causes to exceed the limit only the starting value of range will be printed
    print(any_name)
#for any_name in range(2,3,0.1): ERROR OCCURS AS FLOAT JUMPING IS NOT ALLOWED #TypeError: 'float' object cannot be interpreted as an integer
#for any_name in range(,3,9) or (0,,1) INVLID SYNTAX ERROR OCCURS