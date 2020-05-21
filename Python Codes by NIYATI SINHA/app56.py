#Keyword argument
#the price of one balloon in 4Rs, calculate the cost depending on how many baloons one purchases
def calculation(quantity, price):
    print(f'price={quantity*price}')


#calculation(10,4)
a=int(input("quantity>"))
b=int(input("price>"))
calculation(quantity=a,price =b) #readability of code is increades using keywod argument
