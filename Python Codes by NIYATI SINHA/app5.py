birth_year=input("enter the year of your birth: ")
present_year=input("enter present year: ")
print(int(present_year)-int(birth_year))
#everything entered using the input function is treated as a string thus we need to convert this string to integer
#int(): to convert string to integer
#float(): to convert string to float
#bool(): : to convert string to boolean

#type(): to find the data type
print(type(birth_year))
print(type(int(birth_year)))