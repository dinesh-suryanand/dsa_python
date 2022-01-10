class Shape:
    sname ="Shape"

    def getName(self):
        return self.sname


class XShape(Shape):
    def __init__(self,name) -> None:
        self.xsname = name

    def getName(self):
        return (super().getName()+" "+ self.xsname)


circle = XShape("Circle")
print(circle.getName())


#challenge 2 ...........................

class Animal:
    def __init__(self,name,sound) -> None:
        self.name = name
        self.sound = sound
    
    def Amimal_details(self):
        print(f"{self.name} makes the sound : {self.sound} ")


class Dog(Animal):
    def __init__(self, name, sound,family) -> None:
        super().__init__(name, sound)
        self.family = family
    
    def Amimal_details(self):
        super().Amimal_details()
        print(self.family)

class Sheep(Animal):
    def __init__(self, name, sound , color) -> None:
        super().__init__(name, sound)
        self.color = color
    
    def Amimal_details(self):
        super().Amimal_details()
        print(self.color)


d = Dog("pogo","woof WOOF","Lab")
d.Amimal_details()