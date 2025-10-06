from student import Student
class MedicalStudent(Student):
    def __init__(self, student_id, name, age, percentage, specialization, marks_of_internship):
        super().__init__(student_id, name, age, percentage)
        self.specialization = specialization
        self.marks_of_internship = marks_of_internship

    def accept(self):
        super().accept()
        self.specialization = input("Enter Specialization: ")
        self.marks_of_internship = float(input("Enter Internship Marks: "))

    def display(self):
        super().display()
        print(f"Specialization: {self.specialization}")
        print(f"Internship Marks: {self.marks_of_internship}")

    def calculate_rank(self):
        total = (self.percentage + self.marks_of_internship) / 2
        if total >= 85:
            return "Excellent"
        elif total >= 70:
            return "Good"
        elif total >= 55:
            return "Average"
        else:
            return "Needs Improvement"

    def __str__(self):
        return (f"MedicalStudent({self.student_id}, {self.name}, {self.age}, "
                f"{self.percentage}%, Specialization: {self.specialization}, Internship Marks: {self.marks_of_internship})")
