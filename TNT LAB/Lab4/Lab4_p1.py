a=[] #defining empty list
n=int(input("enter no. of elements to enter in tuple"))
for i in range(n):
    a.append(int(input(f'Enter element {i+1} :')))
print(a) #all elements are added in list
print(type(a))



#finding second largest element in list
a=sorted(a)  #ascending order
# a=sorted(a,reverse=True) #descending order
print(a)
#converting list to tuple
a=tuple(a)
print(a)
print(type(a))

print(f'Second largest element is : {a[-2]}') #ascending order
#descending order a[1] = second largest

