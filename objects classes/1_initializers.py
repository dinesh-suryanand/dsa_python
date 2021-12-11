class Employee:
    def __init__(self,ID,salary, department) -> None:
        self.ID = ID 
        self.salary = salary
        self.department = department
    
# initializing properties

steve = Employee(389,1000,"Human Resource")
steve.title = "Manager"
print("Id :" , steve.ID)
print("salary :", steve.salary)
print("deparmetnt :", steve.department)
print(steve.title)


class EmployeeWithInitializerParameters:
    def __init__(self,ID =None,salary=0, department=None) -> None:
        self.ID = ID 
        self.salary = salary
        self.department = department

mark = EmployeeWithInitializerParameters()
berg = EmployeeWithInitializerParameters("3212",2500 ,"Hr")
print("----------- "*5)
print("Mark")
print(f"id is {mark.ID}")
print(f"salary is {mark.salary}")
print(f"department is {mark.department}")


print("berg")
print(f"id is {berg.ID}")
print(f"salary is {berg.salary}")
print(f"department is {berg.department}")