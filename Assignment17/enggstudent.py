from student import Student
class EnggStudent(Student):
    def __init__(self, student_id, name, age, percentage, branch, internal_marks):
        super().__init__(student_id, name, age, percentage)
        self.branch = branch
        self.internal_marks = internal_marks

    def accept(self):
        super().accept()
        self.branch = input("Enter Branch: ")
        self.internal_marks = float(input("Enter Internal Marks: "))

    def display(self):
        super().display()
        print(f"Branch: {self.branch}")
        print(f"Internal Marks: {self.internal_marks}")

    def calculate_rank(self):
        total = (self.percentage + self.internal_marks) / 2
        if total >= 90:
            return "Distinction"
        elif total >= 75:
            return "First Class"
        elif total >= 60:
            return "Second Class"
        else:
            return "Pass"

    def __str__(self):
        return (f"EnggStudent({self.student_id}, {self.name}, {self.age}, "
                f"{self.percentage}%, Branch: {self.branch}, Internal Marks: {self.internal_marks})")
