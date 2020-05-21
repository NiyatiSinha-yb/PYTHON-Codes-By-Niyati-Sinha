#formatted Strings
first='John'
last='Smith'
# we wanna print: John [Smith] is a coder
message=first+" ["+last+"] is a coder"
print(message) #not ideal to use this
msg=f'{first} [{last}] is a coder' #f'' is used for formatted string
# anything within {} is to access the value of variable mentioned wihin {}
print(msg)