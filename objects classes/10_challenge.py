#23_Challenge_1__Implement_Rectangle_Class_Using_the_Encapsulation


class Rectangle:
    def __init__(self,length, width) -> None:
        self.__length = length
        self.__width = width
    
    def area(self):
        return self.__length * self.__width                 #though they are private the answer is return via area()

    def perimeter(self):
        return (self.__length + self.__width)*2


box = Rectangle(4,5)

print(box.area())


