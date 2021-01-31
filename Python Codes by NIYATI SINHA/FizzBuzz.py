Upperrange=int(input("Upper Range limit : "))

for i in range(1, Upperrange+1, 1):
    flag=0
    if i%3==0:
        flag=1
        print('Fizz',end=' ')
    if i%5==0:
        flag=1
        print('Buzz', end=' ')
    if flag==0:
        print(i, end=' ')
    print("")