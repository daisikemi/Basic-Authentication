class Account:
    def __init__(
            self,
            account_number: str,
            account_type: str, 
            balance: float, 
            account_holder: str,
    ):
        self.account_number = account_number
        self.account_type = account_type
        self.balance = balance
        self.account_holder = account_holder

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount < self.balance:
            self.balance - amount
        else:
            print("insufficient fund")

    def get_balance(self): 
        return self.balance
    
    def get_account_number(self):
        return self.account_number
    
    def get_account_type(self):
        return self.account_type
    
    def get_account_details(self):
        return f"account name: {self.account_holder}, \
              account number {self.account_number}, \
                account balance {self.balance}"
    
class savingsAccount(Account):
        def init (self, account_number, account_holder, balance):
            super().__init__(account_number = account_number, account_type = "savings",
                             balance = balance, account_holder = account_holder)
            
class currentaccount(Account):
        def init (self, account_number, account_holder, balance):
            super().__init__(account_number = account_number, 
                             account_type = "current",
                             balance = balance, 
                             account_holder = account_holder)


           
Ope_savings_account= savingsAccount(
            account_number= "0123756434", 
            balance= 20000000.00, 
            account_type= "savings",
            account_holder= "Opemipo Ogundaisi")

print(Ope_savings_account.get_account_details())


paul_current_account= currentaccount(
             account_number= "4236789072",
             balance= 5000000.00,
             account_type= "current",
             account_holder= "Paul Adeleke"
)
print(paul_current_account.get_account_details())
    