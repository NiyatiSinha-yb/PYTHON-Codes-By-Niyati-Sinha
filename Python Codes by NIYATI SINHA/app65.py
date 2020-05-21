#constructors
class PointIn2D: #naming convetion for classes : start with capital and for more than one word capitalise each first letterof word #class NiyatiSinha
    def __init__(self,x,y):
        self.x=x #self.x means x of the current object
        self.y=y
        self.z=0
       # a="point in 2D plane"
    def move(self):
        print("move")

    def draw(self):
        print("draw")


point=PointIn2D(10,20)
print(f'({point.x},{point.y},{point.z})')