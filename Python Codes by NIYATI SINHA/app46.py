#write a program to remove the duplicates from a list
list=[1,2,4,9,4,5,1,7,1,9]
unique=[]
for items in list:
    if items not in unique:
        unique.append(items)
print(unique)