from pathlib import Path
path=Path()
print(path)
print(path.glob('*')) #for the object generator of all the files and directories (everything)
print(path.glob('*.*')) #for the object generator of all the files in the current directory
print(path.glob('*.py')) #for the object generator of all the .py files in the current directory
print(path.glob('*.xls')) #for the object generator of all the .py files in the current directory
#now lets iterate the object
for file in path.glob('*'):
    print(file)
print("-----------------------------------------------------------------------")
for file in path.glob('*.*'):
    print(file)
print("-----------------------------------------------------------------------")
for file in path.glob('*.py'):
    print(file)
print("-----------------------------------------------------------------------")
for file in path.glob('*.xls'):
    print(file) # nothing printed as no .xls file is present
print("-----------------------------------------------------------------------")

