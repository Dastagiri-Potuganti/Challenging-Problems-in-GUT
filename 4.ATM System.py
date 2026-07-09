class ATM:
    def __init__(self,balance):
        self.__balance=balance
    def deposit(self,amount):
        self.__balance+=amount
        print("Amount Deposited")
    def withdraw(self,amount):
        if amount<self.__balance:
            self.__balance-=amount
            print("Amount Withdrawed")
        else:
            print("Insufficient Balance")
    def balance(self):
        print("Amount in the account is:",self.__balance)

account=ATM(1000)
account.deposit(1000)
account.balance()
account.withdraw(200)
account.balance()
account.withdraw(2222)
