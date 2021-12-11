# there are 3 types of **data members** in python  they are public , private , protectd
#2 types of access modifies

#in general we use public access modifiers only
class Employee:
    def __init__(self,ID,salary):
        self.ID = ID 
        self.salary = salary
    
    def displayID(self):
        print(self.ID)

steve = Employee(3232,10000)
steve.displayID()
print(steve.salary)

#private attributes
# we use ' __ ' before varible example __salary
class EmployeeProtected:
    def __init__(self,ID,salary):
        self.ID = ID 
        self.__salary = salary          #salary is private property 
    
    def displaySalary(self):
        print("Salary :",self.__salary)
    
    def __displayID(self):              # private method
        print(self.ID)


mark = EmployeeProtected(3412,2000000)
mark.displaySalary()
# mark.__displayID()                      #this will genereate an error
print(mark._EmployeeProtected__salary)     #adding ' _ ' before class name will help to access private method


#python doesnot have protected access modifier
