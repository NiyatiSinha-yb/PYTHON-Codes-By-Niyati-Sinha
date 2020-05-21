command=""
while command!="quit":
    command=input('>')
    if command.lower()=='help':
        print("""
start - to start the car
stop - to stop the car
quit - to exit """)    #print("start - to start the car") #print("stop - to stop the car")#print("quit - to exit")
    elif command.lower()== 'start':
        print("Car started...Ready to drive")
    elif command.lower()== 'stop':
        print("Car Stopped.")
    elif command.lower()== 'quit':
        break
    else:
        print("I don't understand")