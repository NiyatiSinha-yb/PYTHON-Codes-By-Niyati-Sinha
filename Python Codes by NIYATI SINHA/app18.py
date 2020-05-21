price=1000000
is_goodcredit=False
is_goodcredit=True
print(is_goodcredit)
if is_goodcredit:
    print("Put down price by 10%")
    #price=price-0.1*price
    downpayment=0.1*price
    price-=0.1*price
    #print(price)
else:
    print("Put down price by 20%")
    # price=price-0.2*price
    downpayment = 0.1 * price
    price -= 0.2 * price
    #print(price)
print(f'Price:{price}')
print(f'Down payment:{downpayment}')