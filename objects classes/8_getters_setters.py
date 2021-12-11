#they are help to access private properties 
# encapsulation can be achieved via getters and setters

class User:
    def __init__(self,userName = None) -> None:
        self.__userName = userName
    
    #setter
    def setUserName(self,x):
        self.__userName = x
    
    #getter
    def getUserName(self):
        return self.__userName


steve = User("Steve_Rogers06")

print("Befor Setting : ",steve.getUserName())

steve.setUserName('Steve_06')

print("After Setting", steve.getUserName())