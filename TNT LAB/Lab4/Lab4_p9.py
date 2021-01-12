def input_tuple():
    a = []  # defining empty list
    n = int(input("enter no. of subjects to enter in tuple"))
    for i in range(n):
        a.append(input(f'Enter element {i + 1} :'))
    print(a)  # all elements are added in list
    print(type(a))
    a = tuple(a)
    print(a)
    print(type(a))
    return a

input_tuple()