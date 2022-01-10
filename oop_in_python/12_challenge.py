#1st challenge easy to compled and completed but delete ipoidi 
#challane 2 lo challage 1 undi so no problem    

class Account:
    def __init__(self,title=None , balance = 0) -> None:
        self.title = title
        self.balance = balance
    
    def withdraw(self,amount):
        self.balance = self.balance - amount

    def deposit(self,amount):
        self.balance = self.balance + amount

    def getBalance(self):
        return self.balance

class SavingsAccount(Account):
    def __init__(self, title=None, balance=0,intrestRate=0) -> None:
        super().__init__(title=title, balance=balance)
        self.intrestRate = intrestRate

    def intrestAmount(self):
        return (self.intrestRate * self.balance/100)


demo1 = SavingsAccount("Steve",5000,10)
print("Initial Balance : " ,demo1.getBalance())
demo1.withdraw(1000)
print("Balance after withdraw of 1000 is :" ,demo1.getBalance())
demo1.deposit(1500)
print("Balance after deposit of 1500 is",demo1.getBalance())

print("Intrest on current balance :",demo1.intrestAmount())