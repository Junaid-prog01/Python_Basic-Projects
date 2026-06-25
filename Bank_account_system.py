class Bank :
    def __init__(self, name, acc_no, balance):
        self.name = name
        self.acc_no = acc_no
        self.balance = balance
    
    def __str__(self):
        return "this dudler is workong"
    def check_bal(self):
        print(f"Your balance is {self.balance}")
    
    def deposit(self, amount):
        self.balance += amount
        return f"Your Balance is {self.balance}"
    
    def withdraw(self, withdraw_m):
        if withdraw_m > self.balance:
            return "Insufficient funds"
        self.balance -= withdraw_m
        return f"Your balance is {self.balance}"
    

man1 = Bank("json", 45259575, 10000)                                                 
print(man1)
