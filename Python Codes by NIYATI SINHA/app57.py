#KEYWORD ARGUMENTS#functions
#when we use : at the end of line , we are telling Python that we are defining a block of code
#function calling is done after function defination as PYTHON uses a Interpreter i.e. one statement after other is executed

def greet_user(fname,lname,age):#defining a function named greet_user
    #write the fname of function in smallcase, when more than one word in function name use _ to seperate words
    print(f"Hi {fname} {lname} of age {age}")
    print("WELCOME TO FUNCTIONS") #after a function in Python the best practice is to leave two lines


print("going to call the function")
greet_user("Niyati",lname="SINHA",age=20)#calling function using keyword Argument
#thus when using both positional and keyword argument it is limited to using the first arhguments as positional and later arguments as keyword
print("function call finished")#always use postional (normal) aruments first and then the keyword arguments