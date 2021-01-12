#tuple 1
def input_tuple():
    a = []  # defining empty list
    n = int(input("enter no. of elements to enter in tuple"))
    for i in range(n):
        a.append(int(input(f'Enter element {i + 1} :')))
    print(a)  # all elements are added in list
    print(type(a))
    a = tuple(a)
    print(a)
    print(type(a))
    return a

tuple1=input_tuple()
tuple2=input_tuple()
print(f'tuple1={tuple1}, tuple2={tuple2}')
tuple1,tuple2 = tuple2,tuple1
print(f'tuple1={tuple1}, tuple2={tuple2}')

