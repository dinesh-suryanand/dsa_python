class User:
    def __init__(self,userName,pswrd) -> None:
        self.__userName = userName
        self.__pswrd = pswrd

    def login(self,userName,pswrd):
        if((self.__userName.lower() == userName.lower()) and (self.__pswrd == pswrd)):
            print("Access Granted for : ",self.__userName,"and password is : " ,self.__pswrd)
        else:
            print("Invalid Credentials!")

#creating steve object
steve = User("steve","12345")

steve.login("steve","12345")        #grants access beacuse credentials are valid

steve.login("steve","332324")       #dont grant access since credentials are invalid

# steve.__pswrd       #compaliatin error