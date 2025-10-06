from enggstudent import EnggStudent
from medicalstudent import MedicalStudent
from college import College


c1 = College("Tech University")
s1 = EnggStudent(101, "Rahul", 21, 85, "Computer", 90)
s2 = MedicalStudent(102, "Sneha", 22, 78, "Cardiology", 82)

c1.add_student(s1)
c1.add_student(s2)
c1.display_all()
print(s1.name, "Rank:", s1.calculate_rank())
print(s2.name, "Rank:", s2.calculate_rank())
