def createfibonacci(first,second,no_of_terms):
    list=[first,second]
    for k in range (no_of_terms-2):
        next=first+second
        first=second
        second=next
        list.append(second)
    return tuple(list)

no=int(input('no. of terms to be founded in Fibonacci Series'))
first=int(input('first term of the Fibonacci Series'))
second=int(input('second term of the Fibonacci Series'))
a=createfibonacci(first,second,no)
print(a)

