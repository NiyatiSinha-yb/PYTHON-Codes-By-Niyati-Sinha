def input_tup():
    a = []  # defining empty list
    n = (int(input("enter no. of elements to enter in tuple")))
    for i in range(n):
        a.append(input(f'Enter element {i + 1} :'))
    a = tuple(a)
    print(type(a))
    return a

tuple1=input_tup()
tuple2=input_tup()

print(f'tuple1={tuple1}, tuple2={tuple2}')
tuple1,tuple2 = tuple2,tuple1
print(f'tuple1={tuple1}, tuple2={tuple2}')
