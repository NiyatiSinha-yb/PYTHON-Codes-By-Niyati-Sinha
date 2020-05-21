course="Python for beginners"
print(len(course))
print(course)
upper=course.upper() #this function does not change the string but returns a new string
print(upper)
lower=course.lower()
print(lower)

print(course.find('P'))#it will return the index of first P in the string
print(course.find('o'))
print(course.find('Z'))# when the argument passed to find() function is not present it returns -1
print(course.find('ton'))# we can also search for a sequence of characters
river="MISSISSIPPI"
print(river.find("ISSI"))# returns the index of first position of ISSI from tyhe string where it firstly finds ISSI
print(course.replace('beginners','Absolute beginners '))
print(course.replace('P','J'))
print('Python' in course) #returns boolean