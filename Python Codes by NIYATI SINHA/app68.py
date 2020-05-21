class Mammal:#inheritance
    def walk(self):
        print("walk")


class Dog(Mammal): #dog inherits Mammal class, Thus Dog: child class , Mammal: parent class
    def __init__(self):
        print("I am a Dog")
    def bark(self):
        print("I can Bark")


class Cat(Mammal):
    def __init__(self):
        print("I am a cat")
    def meow(self):
        print("Meow...")

obj=Mammal()
obj.walk()
dog1=Dog()
dog1.walk()
dog1.bark()
cat1=Cat()
cat1.walk()
cat1.meow()
obj=Mammal()
obj.walk()