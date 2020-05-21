#exceptions #try: #accept:
try:
    age=int(input('Age: '))
    income=12000000
    risk=income/age
    print(age)
except ZeroDivisionError:
    print("Age cannot be zero")
except ValueError: # if during the execution of the try block VakueError is encountered then this except block will be executed
    print("Invalid Value entered")