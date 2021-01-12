def getPowers(x):
    a=[]
    a=[x,x**2,x**3,x**4]
    print(type(a))
    b=tuple(a)
    print(type(b))
    return (tuple(a))

n=5
a=()
print(f'Input {n} numbers')
for i in range(n):
    print(getPowers(int(input(f'enter {i+1} numbers : '))))
    print("\n")