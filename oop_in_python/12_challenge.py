class Account:
    def __init__(self,title=None,balance=0) -> None:
        self.title = title
        self.balance = balance

class SavingsAccount(Account):
    def __init__(self, title=None, balance=0,intrestRate =0) -> None:
        super().__init__(title, balance)
        self.intrestRate = intrestRate

mark = Account("mark",5000)

mamo = SavingsAccount("mark",5000,5)