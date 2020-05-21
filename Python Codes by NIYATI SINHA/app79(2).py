import random


class Dice:  #now no warning for line space
    def roll(self): #returns a tuple # immutable #()
        first=random.randint(1,6)
        second=random.randint(1,6)
        return first, second #this will return a tupple # wheen we return without brackets in Python it automatiocally returns a tupple
        #return (first, second)


dice=Dice()
a=dice.roll()
print(type(a))
print(a)
