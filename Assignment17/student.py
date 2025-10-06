# Q1.Create a class Student with following  
# a.  data members :   
# i. StudentId 
# ii.  Name 
# iii. Age
# iv. percentage
# b. Add the following methods : 
# i. Parameterized constructor 
# ii. Display
# iii. Accept
# iv. Method  calculateRank
# v. Override  __str__Method

class Student:
    def __init__(self, student_id, name, age, percentage):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.percentage = percentage

    def accept(self):
        self.student_id = input("Enter Student ID: ")
        self.name = input("Enter Name: ")
        self.age = int(input("Enter Age: "))
        self.percentage = float(input("Enter Percentage: "))

    def display(self):
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Percentage: {self.percentage}%")

    def calculate_rank(self):
        if self.percentage >= 90:
            return "A+"
        elif self.percentage >= 75:
            return "A"
        elif self.percentage >= 60:
            return "B"
        elif self.percentage >= 50:
            return "C"
        else:
            return "Fail"

    def __str__(self):
        return f"Student({self.student_id}, {self.name}, {self.age}, {self.percentage}%)"
