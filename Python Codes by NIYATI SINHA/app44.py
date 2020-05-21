numbers=[5,2,1,7,4]
numbers.append(20) #insert at the end
print(f"insert at the end {numbers}")
numbers.insert(0,10) # insert(a,b) means insert item b at the index a
print(f"insert item b at the index a {numbers}")
print(f"index of the first occurance of the passed item: {numbers.index(5)}")#returns the index of the first occurance of the passed item
numbers.remove(5) #pass the item you want to remove
print(numbers)
numbers.pop()#to remove the last item in the list
print(numbers)
numbers.clear() #to empty our list, that is, to remove all the elements of the list
print(numbers)
#print(numbers.index(5))#returns the index of the first occurance of the passed item #error #ValueError: 5 is not in list