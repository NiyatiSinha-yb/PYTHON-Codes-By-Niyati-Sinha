#unpacking # can be applied to list and tuples both
coordinates=(1,2,3)
#coordinates[0]*coordinates[1]*coordinates[2]
#x=coordinates[0]
#y=coordinates[1]
#z=coordinates[2]
x,y,z=coordinates # PYTHON INTERPRETER ASSIGNS THE FIRST VARIABLE IN THE TUPLE TO X THEN SECOND TO Y AND SO ON.
#A,B=coordinates # this gives error #ValueError: too many values to unpack (expected 2)
A,B,C=coordinates
print(f'({x},{y},{z})')
print(f'A={A}, B={B}')