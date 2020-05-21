#exceptions #try: #accept:
try:
    age=int(input('Age: '))
    print(age)
except ValueError: # if during the execution of the try block VakueError is encountered then this except block will be executed
    print("Invalid Value entered")