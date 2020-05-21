#files and directories
from pathlib import Path

#THERE ARE TWO TYPES OF PATH
#1 ABSOLUTE PATH: eg. Windows     C:\Users\KIIT\PycharmProjects\Project1 , LINUX/MAC     /usr/local/bin
#2 RELATIVE PATH:

path= Path("eccomerce")
print(path.exists())# if this python directory exists is prints True else False
path2= Path("emails")
print(path2.exists()) #as it prints false this means this directory does not exist yet
path2.mkdir() #this function creates emails directory
print(path2.exists()) #now it exists