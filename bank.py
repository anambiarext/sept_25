class Account:
    def __init__(self,acc_number, name, balance):
        self.acc_number = acc_number
        self.name = name
        self.balance = balance
    
    def Balance(self):
        print("Balance : ",self.balance)
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
        
        else:
            print("Insufficient Balance")

acc1 = Account(101,"ram",5555)
acc1.Balance()

acc1.withdraw(25)
acc1.Balance()

acc1.deposit(470)
acc1.Balance()

acc1.withdraw(6001)
