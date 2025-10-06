class College:
    def __init__(self, college_name):
        self.college_name = college_name
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        print(f"Student {student.name} added successfully!")

    def get_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    def remove_student(self, student_id):
        student = self.get_student(student_id)
        if student:
            self.students.remove(student)
            print(f"Student {student.name} removed successfully!")
        else:
            print("Student not found!")

    def display_all(self):
        print(f"\nCollege: {self.college_name}")
        for student in self.students:
            print(student)

    def __str__(self):
        return f"College({self.college_name}, Total Students: {len(self.students)})"
