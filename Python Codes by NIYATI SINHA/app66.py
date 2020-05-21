class Person:
    def __init__(self,my_name):
        self.name=my_name

    def talk(self):
        print(f'Hey! I am {self.name}' )


a=input("enter your name ")
object_variable1=Person(a)
object_variable1.talk()

b=input("enter your name ")
object_variable2=Person(b)
object_variable2.talk()
