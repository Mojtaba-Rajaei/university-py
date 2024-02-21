
class MinimalClass:
    pass

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

def whereIs(point):
    match point:
        case Point(0,0):
            print({"x":point.x,"y":point.y})
        case Point(0,y):
            print(f"X:{point.x},Y:{point.y}")
        case _:
            raise ValueError("I don't know what the fuck is this")

def initLog(*arg):
    pass # implement later

while True:
    initLog()
    pass 

