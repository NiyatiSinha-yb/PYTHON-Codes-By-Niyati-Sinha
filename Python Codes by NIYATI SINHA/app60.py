#creating a Reusable Function
def emoji_convertor(message):
    words_list = message.split(" ")  # split the string whenever it finds a space and returns a list
    #print(words_list)
    emojis = {":)": "😊", ":(": "😟", ":D": "😃", ":|": "😐"}
    output = ""
    for item in words_list:
        output += emojis.get(item,item) + " "  # emojis.get() looks for the value of the key i.e. item and if the key is not present then it returns item itself
    return output


result=emoji_convertor(input(">"))
print(result)
