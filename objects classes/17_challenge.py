from _typeshed import Self


class Car:
    def __init__(self,model,color) -> None:
        self.model = model
        self.color = color

    def printDetails(self):
        print(f"model of car is {self.model}, the color is {self.color}")

class SedanEngine:
    def start():
        print(" Car has stated")
    def stop():
        print(" Car has stopped")


class Sedan(Car):
    def __init__(self, model, color,engine) -> None:
        super().__init__(model, color)
        self.engine = engine
    
    def setStart(self):
        self.engine
