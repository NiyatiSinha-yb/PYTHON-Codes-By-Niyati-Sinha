#inheritance
class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal): #dog inherits Mammal class, Thus Dog: child class , Mammal: parent class
    pass #pass is written when the class is empty (no code written in it)


class Cat(Mammal):
    def __init__(self):
        print("I am a cat")


dog1=Dog()
dog1.walk()
cat1=Cat()
cat1.walk()
obj=Mammal()
obj.walk()