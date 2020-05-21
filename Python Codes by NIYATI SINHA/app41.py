#write a program to find the largest and smallest no in the list
Elements=[1,2,4,2,1,0,7,8,9,3,2,-1,11,2,3,4,0,-2,2,4,6,-1]
max=Elements[0]
min=Elements[0]
for item in Elements:
    if item > max:
        max=item
    elif item < min:
        min=item
print(f'MAX={max} and MIN={min}')