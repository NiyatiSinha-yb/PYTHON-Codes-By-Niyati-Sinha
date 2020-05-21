numbers=[5,2,1,5,7,4]
print(50 in numbers) #will check for existance of a or sequence of characters in a string
#True when element is present and false when not present
print((2 in numbers))
print(numbers.count(5))#returns how many times a given item is present in the list
print(numbers.count(-1))#returns how many times a given item is present in the list
numbers.sort()#sorts our list, sorts the original list #ascending order
print(numbers)
numbers.reverse()#after using the sort function if we reverse the list we get descending order
print(numbers)
copy_num=numbers.copy() #function to copy numbers list to copy_num list
print(copy_num)
#now if we make any changes to numbers list, it is gonna do no impact on copy_num list
