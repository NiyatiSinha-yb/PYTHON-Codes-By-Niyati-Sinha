#functions
#when we use : at the end of line , we are telling Python that we are defining a block of code
#function calling is done after function defination as PYTHON uses a Interpreter i.e. one statement after other is executed

def greet_user(fname,lname):#defining a function named greet_user
    #write the fname of function in smallcase, when more than one word in function name use _ to seperate words
    print(f"Hi {fname} {lname}")
    print("WELCOME TO FUNCTIONS") #after a function in Python the best practice is to leave two lines


print("going to call the function")
greet_user("Niyati","Sinha")#calling function
print("function call finished")