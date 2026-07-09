class library:
    def __init__(self,name,author,price):
        self.name=name
        self.author=author
        self.price=price
    def display(self):
        print("Book name is:",self.name)
        print("Book Author is :",self.author)
        print("Book Price is:",self.price)
        print()

b1=library('Python','Srinivas Sir',2000)
b2=library('MYSQL','Dastagiri',1500)
b3=library("React",'Harish',1450)

b1.display()
b2.display()
b3.display()