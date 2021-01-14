def input_to_dict(key):
    if key in dict:
        dict[key]+=1
    else:
        dict[key]=1

def print_sort_wordFreq():
    sort_dict=sorted(dict,key=dict.get, reverse=False) #ascening order
    print(sort_dict)

dict={}
word=(input(f'Input word: '))
word=word.lower()
for alphabet in word:
    input_to_dict(alphabet)

print(dict)
print_sort_wordFreq()