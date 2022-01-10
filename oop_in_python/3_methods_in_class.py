#implementing methonds in class
# 3 types of methods in a class

# instance method example
from typing import ClassVar


class Employee:
    def __init__(self,ID =None,salary=0, department=None) -> None:
        self.ID = ID 
        self.salary = salary
        self.department = department

    #methods  #instance methods  # most common menthods
    def tax(self):
        return(self.salary * 0.2)
    def salaryPerDay(self):
        return(self.salary / 30)

steve = Employee(9292,10000,"pAt")

print(f"Tax payed by steve {steve.tax()}")
print(f"Salary per day is  {steve.salaryPerDay()}")






#class method example 
class MyClass:
    teamName = 'liverpool'

    def __init__(self,name) -> None:
        self.name =name

    @classmethod    # this is called decorator
    def getTeamName(cls):                      # instance varible we self as paramter , here we use cls <------- convention
        return cls.teamName

print(MyClass.getTeamName()) 






#static method example
#we can pass as many as argumetns in static method  <------------------- cool thing
class Player:
    teamName = 'liverpool'

    def __init__(self,name) -> None:
        self.name =name

    @staticmethod    # this is called decorator
    def demo():
        print("I am Static Method")

p1 = Player('101')
p1.demo()
Player.demo()

#static method use case example

class BodyInfo:
    @staticmethod
    def bmi(weight, height):
        return weight/(height**2)

weight = 75
height = 1/8
print(BodyInfo.bmi(weight, height))