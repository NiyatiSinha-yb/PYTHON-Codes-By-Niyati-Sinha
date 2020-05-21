#classes
class Point: #naming convetion for classes : start with capital and for more than one word capitalise each first letterof word #class NiyatiSinha
    def move(self):
        print("move")

    def draw(self):
        print("draw") # now the class is finished so remove further indentation and leave 2 lines space


point1=Point()#object Point() is stored in a variable point1
print(type(point1))
point1.draw()
