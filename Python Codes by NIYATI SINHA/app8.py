#using indexes in string
#index  0123456789...
course='Python for beginners' #reverse index    ...-3 -2 -1  ; -1 for s, -2 for r, ...
print(course[0])
print(course[-1])
print(course[-2])

print(course[0:3]) #all the character starting from index 0 to 2 as the upper limit is not inclusive
print(course[1:3])

print(course[0:]) #if the upper limit is not mentioned then it will return all the characters till the end of string
print(course[1:])

print(course[:6]) # if the lower limit is not mentioned Python will treat 0 as the starting index
print(course[:-1])# whole string except the the last character "S"
print(course[:0]) #return string starting from char 0 going upto 0 thus nothing is returned
print(course[:]) #this is used to copy or clone the whole string
copy_course=course[:]
print(copy_course)