dict={'a':'#', 'e':'@','i':'$','o':'%','u':'!'}
word=(input(f'Input word: '))
list=[]
for alphabet in word:

    if alphabet in dict:
        list.append(dict[alphabet])
    else:
        list.append(alphabet)

for char in list:
    print(char,end="")