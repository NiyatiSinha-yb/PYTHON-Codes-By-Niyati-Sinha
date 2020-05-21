#input phone no in numbers and convert it to words
dictionary={"1":"ONE","2":"TWO","3":"THREE","4":"FOUR","5":"FIVE", "6":"SIX","7":"SEVEN","8":"EIGHT","9":"NINE","0":"ZERO"}
output=""
phone=input('PHONE:')
for values in phone:
    output+=dictionary.get(values," ! ")+" "
print(output)