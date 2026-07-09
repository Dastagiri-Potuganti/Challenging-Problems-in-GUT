class Salary:
    def __init__(self,amount):
        self.__amount=amount
    def set_salary(self,amount):
        self.__amount=amount
        print("Salary Updated")
    def get_salary(self):
        print("Current Salary is:",self.__amount)

emp=Salary(30000)
emp.get_salary()
emp.set_salary(20000)
emp.get_salary()