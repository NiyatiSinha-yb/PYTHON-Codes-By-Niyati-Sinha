tuple=('Toyota','Honda','GM','Ford','BMW','Volkswagon','Mercedes','Ferrai','Porshe')
word=('zero','one','two','three','four','five','six','seven','eight','nine')
print(tuple[2:7])
for element in tuple[2:7]:
    print(f'{word[tuple.index(element)]} : {element}')
