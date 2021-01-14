def input_to_dict(key,value):
    dict[key]=value

def sort():
    sort_dict = sorted(dict, key=dict.get, reverse=True)  # descening order
    print(sort_dict)

dict={}
n=int(input("Input no. of items you students you want to add to dictionary"))
for count in range(n):
    name=input(f'Input name {count} : ')
    marks=input(f'Input marks : ')
    input_to_dict(name,marks)
sort()
