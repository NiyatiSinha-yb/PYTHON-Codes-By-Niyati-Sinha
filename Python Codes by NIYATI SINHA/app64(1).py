#classes
class Point: #naming convetion for classes : start with capital and for more than one word capitalise each first letterof word #class NiyatiSinha
    def move(self):
        print("move")

    def draw(self):
        print("draw") # now the class is finished so remove further indentation and leave 2 lines space


point1=Point()#object Point() is stored in a variable point1
point1.x=10
point1.y=20
print(point1.x)
point1.draw()
point2=Point()
point2.x=100
print(point2.x)