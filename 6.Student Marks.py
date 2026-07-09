class Marks:
    def __init__(self,marks):
        self.__marks=marks
    def get_marks(self):
        print("Student Marks are:",self.__marks)
    def update_marks(self,marks):
        self.__marks=marks
        print("Marks Updated")

student=Marks(56)
student.get_marks()
student.update_marks(60)
student.get_marks()