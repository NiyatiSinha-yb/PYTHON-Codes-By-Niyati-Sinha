a=input("Enter 1st no.")
b=input("Enter 2nd no.")
c=input("Enter 3rd no.")
print(type(a))
if a+b>c or b+c>a or c+a>b: #automatic type conversion from string to int as matehematical operation is performed
    if a==b==c:
        print("Equilateral")
    elif (a!=b and a!=c and b!=c):
        print("Scalene")
    else:
        print("Isoscelus")
else:
    print("Triangle not possible")
