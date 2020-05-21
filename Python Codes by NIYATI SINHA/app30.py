command=""
present_car_status=False # True if started and False if stopped
while True:
    command=input('>')
    if command.lower()=='help':
        print("start - to start the car")
        print("stop - to stop the car")
        print("quit - to exit")
    elif command.lower()== 'start' and present_car_status==False:
        print("Car started...Ready to drive")
        present_car_status=True
    elif command.lower()=='start': #elif command.lower()== 'start' && present_car_status==True:
        print("Car is already started")
    elif command.lower()== 'stop'and present_car_status==True:
        print("Car Stopped.")
        present_car_status=False
    elif command.lower()== 'stop' and present_car_status==False: #elif command.lower()=='stop'
        print("Car already Stopped.")
    elif command.lower()== 'quit':
        break
    else:
        print("I don't understand")