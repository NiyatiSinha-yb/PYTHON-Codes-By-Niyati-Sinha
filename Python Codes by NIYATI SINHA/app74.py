#find the largest no in the list
#using modules
#two modules were imported in module app74_min_max and now we have imported this app74_min_max module here
#the modules which were imported in app74_min_max will not be accessible here and will need to be imported seperately
import app74_min_max

string=input("enter list elements seperated by space: ")
list1=string.split(" ")
print(app74_min_max.find_max(list1))
print(app74_min_max.find_min(list1))