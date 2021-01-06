salary=int(input("Enter your salary"))
#print(type(salary))
if salary<=10000:
    post="clerk"
elif salary<=20000:
    post="Operator"
elif salary<=35000:
    post="Assistant"
elif salary<=50000:
    post="Manager"
else:
    post="Invalid"
print(post)
