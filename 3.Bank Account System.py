class Bank:
    def __init__(self,name,account,amount):
        self.name=name
        self.account=account
        self.amount=amount
    def bank_account(self):
        print("Account Holder Name:",self.name)
        print("Account Number:",self.account)
        print("Balance amount:",self.amount)
        print()

a1=Bank('Giri',25809756432,40)
a2=Bank('Hari',89755743289,2000)
a3=Bank('Srinu',9865765473972,100000)

a1.bank_account()
a2.bank_account()
a3.bank_account()