def input_to_dict(key):
    key=key.lower()
    if key in dict:
        dict[key]+=1
    else:
        dict[key]=1

def print_common_words():
    for word in dict:
        if dict[word]>1:       #dict[word] refers to frequency
            print(f'Common Word :{word}')

dict={}
n=int(input("Input no. of items you words you want to add to dictionary"))
print(dict)
print_common_words()

