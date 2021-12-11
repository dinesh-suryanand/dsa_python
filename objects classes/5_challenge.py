#Implementing  a point Class "Point" 

class Point:
    def __init__(self,a,b,c) -> None:
        self.a = a
        self.b = b
        self. c = c
    def sqsum(self):
        x = self.a **2
        y = self.b **2
        z = self.c **2
        return(x + y + z)

obj = Point(1,3,5)

print(obj.sqsum())