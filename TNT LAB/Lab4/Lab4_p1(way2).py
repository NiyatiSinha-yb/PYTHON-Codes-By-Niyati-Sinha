def secondLargest(T):
    sort_T=sorted(T)
    print(f'sorted tuple {sort_T}')
    return sort_T[-2]

a=[] #defining empty list
n=int(input("enter no. of elements to enter in tuple"))
for i in range(n):
    a.append(int(input(f'Enter element {i+1} :')))
print(a) #all elements are added in list
print(type(a))
T=tuple(a)
print(secondLargest(T))

