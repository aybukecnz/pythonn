

class Student:
    def __init__(self):
        self.name = ""
        self.rollnum = 0
        self.marks = [0, 0, 0]

    def input_data(self):
        self.name = input("Enter name: ")
        self.rollnum = int(input("Enter roll number: "))
        for i in range(3):
            self.marks[i] = int(input(f"Enter {i+1}. mark: "))

    def display_data(self):
        print("Name:", self.name)
        print("Roll number:", self.rollnum)
        print("Marks in three subjects:", end=" ")
        for mark in self.marks:
            print(mark, end=" ")
        print()

student = Student()
student.input_data()
print("Student's information:")
student.display_data()





