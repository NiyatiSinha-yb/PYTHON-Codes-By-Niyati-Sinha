a=[] #defining empty list
n=int(input("enter no. of elements to enter in tuple"))
for i in range(n):
    a.append(int(input(f'Enter element {i+1} :')))
print(a) #all elements are added in list
print(type(a))
a=tuple(a)
print(a)
print(type(a))

sorted_a=sorted(a)
print(f'min={sorted_a[0]}, max={sorted_a[-1]}')