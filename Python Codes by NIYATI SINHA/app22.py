#comparision operators in python
temp=int(input('temperature '))
if temp > 30:
   # print("It's a hot day with temp "+temp)
   print(f"It's a hot day with temp: {temp}")
elif temp<10:
    #print("it's neither a hot day nor a cold day with temp "+temp)
    print(f"it's neither a hot day nor a cold day with temp: {temp}")
elif temp==30: #elif temp=30: will produce error as = is an assignment operator
    print(f'temp: {temp}')
else:
    #print("It's not a hot day with temp "+ temp)
    print(f"It's not a hot day with temp: {temp}")
if temp!=0:
    print("it is not 0 degrees ")