# polymorphism using methods....................
class Rectangle():
    def __init__(self,length=0, breadth=0) -> None:
        self.length = length
        self.breadth = breadth
        self.sides = 4
    
    def getArea(self):
        return (self.length * self.breadth)

class Circle:
    def __init__(self,radius=0) -> None:
        self.radius = radius
        self.sides = 0
    
    def getArea(self):
        return (self.radius * self.radius * 3.142 )



shapes = [Rectangle(2,4),Circle(3)]

print("The sides of Rectangle are :",str(shapes[0].sides))
print("The sides of Circle are :",str(shapes[1].sides))


print("Area of circle is :",str(shapes[1].getArea()))
print("Area of Rectangle is :",str(shapes[0].getArea()))


# Polymorphism using Inheritance.................
print()
print("Polymorphism using Inheritance")
print("Polymorphism using methiod overloading as well")

class Shape:
    def __init__(self) -> None:
        self.sides = 0
    
    def get_area(self):
        pass

class RectangeInherits(Shape):
    def __init__(self,width,length) -> None:
        super().__init__()
        self.width = width
        self.length = length
        self.sides = 4
    
    def get_area(self):
        return (self.width * self.length)

class CircleInherit(Shape):
    def __init__(self,radius) -> None:
        super().__init__()
        self.radius = radius
        self.sides = 4
    
    def get_area(self):
        return (self.radius * self.radius * 3.142)

shapes2 = [RectangeInherits(4,5) , CircleInherit(7)]

print("Area of circle is :",str(shapes2[1].get_area()))
print("Area of Rectangle is :",str(shapes2[0].get_area()))

#Operator over loading..............
print()
print("Polymorphism using operator overloading")

# let us take an example of complex number additon and subtraction a+ib , a - ib <--- complex nums

class Com:
    def __init__(self,real=0,imagi=0) -> None:
        self.real = real
        self.imagi = imagi

    def __add__(self,other):
        temp = Com(self.real + other.real , self.imagi + other.imagi)
        return temp
    
    def __sub__(self,other):
        temp = Com(self.real - other.real , self.imagi - other.imagi)
        return temp

obj1 = Com(5,3)
obj2 = Com(4,8)
obj3 = obj1 + obj2
obj4 = obj1 - obj2

print(f"obj3 is : {obj3.real} + {obj3.imagi}i")
print(f"obj4 is : {obj4.real} + ({obj4.imagi})i")


#duck typing ................ sounds funny
#implementaion of duck typing 
class Dog:
    def speak(self):
        print("woof , woof")

class Cat:
    def speak(self):
        print("mewo , meow")

class AnimalSound:
    def sound_func(self,animal):
        animal.speak

sound = AnimalSound()
dog = Dog()
cat = Cat()

sound.sound_func(dog)
sound.sound_func(cat)

#we can inplement polymorphism typing by using dynamic typing 