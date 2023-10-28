#banking system program
class BankAccount:
    def __init__(self, account_number, balance, date_of_opening, customer_name):
        self.account_number=account_number
        self.balance=balance
        self.date_of_opening=date_of_opening
        self.customer_name=customer_name
    def deposit(self):
        depositing_amount=int(input("enter the amount you want to deposit :"))
        self.balance=self.balance+depositing_amount
        print(f"you have successfully deposited Kes {depositing_amount} your current balance is Kes {self.balance}")
    def withdraw(self):
        withdrawing_amount=int(input("enter the amount you want to withdraw:"))
        if self.balance < withdrawing_amount:
            print("you have insufficient balance.your account balance is",self.balance)
        else:
            self.balance=self.balance-withdrawing_amount
            print(f"you have successfully withdran {withdrawing_amount} your current remaining balance is {self.balance}")
    def check_balance(self):
        print("your current bank balance is Kes",self.balance)
    def customer_details(self):
        print(f"dear {self.customer_name} your account number is {self.account_number} opened on {self.date_of_opening} and the current balance is {self.balance}")
bankaccount=BankAccount(110890714785432, 14000, "10th June 2014", "Kelly Chris")
print(bankaccount.deposit())
print(bankaccount.withdraw())
print(bankaccount.check_balance())
print(bankaccount.customer_details())
