#TUPLES
#tuples are immutable
#we can not add new items nor can we remove existing items in tuples unlike lists
numbers=(1,2,3)
#tuples only support two functions count() and index() as we can't alter the tuples so no functions like append() pop() for it
print(numbers.count(3))
print(numbers.count(-1))
print(numbers.index(3))
#print(numbers.index(10)) #ValueError: tuple.index(x): x not in tuple
print(numbers[0])#item atv first index in tuple
#numbers[0]=10 #error TypeError: 'tuple' object does not support item assignment