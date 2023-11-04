#prolog
# Author: Darling Ngoh 
# Email: dngoh1@student.gsu.edu
# Group: ACS49
'''
Purpose:
    A bank account management program.
'''

class BankAccount:
    def __init__(self,new_name,checking_balance, savings_balance):
        # TODO: Define constructor with parameters to initialize instance attributes        
        self.customer_name = new_name
        self.chcking_balance = checking_balance
        self.savings_acct = savings_balance
# TODO: Define deposit_checking() method
    def deposit_checking(self, amount):
        if amount > 0:
            checking_balance += amount
        else:
            print ("Only amounts greater than $0")
# TODO: Define deposit_savings() method
    def deposit_savings(self, amount):
        if amount > 0:
            savings_balance += amount
        else:
            print ("Only amounts greater than $0")
# TODO: Define withdraw_checking()  method
    def withdraw_checking(self, amount):
        if self.checking_balance > amount:
            self.checking_balance -= amount
        else:
            print("Checking account must be positive in order to withdraw")
# TODO: Define withdraw_savings()  method
    def withdraw_savings(self, amount):
        if self.savings_balance >= amount:
            self.savings_balance -= amount
        else:
            print("Savings account must be positive in order to withdraw")
        
# TODO: Define transfer_to_savings() method
    def transfer_to_savings(self, amount):
        if self.checking_balance >= amount:
            self.checking_balance -= amount
            self.savings_balance += amount
        else:
            print("Checking account must be positive in order to transfer to savings")

#Demo code
account = BankAccount("Mickey", 500.00, 1000.00)    
account.checking_balance = 500    
account.savings_balance = 500    
account.withdraw_savings(100)    
account.withdraw_checking(100)    
account.transfer_to_savings(300)

print(account.customer_name)    
print(f'${account.checking_balance:.2f}')    
print(f'${account.savings_balance:.2f}')

