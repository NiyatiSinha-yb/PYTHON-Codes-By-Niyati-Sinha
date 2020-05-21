#find the largest no in the list
#using modules

import app72_find_max
import app72_find_min

string=input("enter list elements seperated by space: ")
list1=string.split(" ")
print(app72_find_max.find_max(list1))
print(app72_find_min.find_min(list1))