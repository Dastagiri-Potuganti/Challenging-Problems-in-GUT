class student:
    def __init__(self,name,roll_no,marks):
        self.name=name
        self.roll_no=roll_no
        self.marks=marks
    def display(self):
        print("Student Name:",self.name)
        print("Student Roll_no:",self.roll_no)
        print("Student Marks:",self.marks)
        print()
s1=student('giri',10,99)
s2=student('dheeraj',20,88)
s3=student('anil',30,77)
s1.display()
s2.display()
s3.display()