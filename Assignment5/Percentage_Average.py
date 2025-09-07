# students = int(input("Enter number of students: "))
# total_percent = 0

# for i in range(students):
#     marks = 0
#     for j in range(5):
#         marks += int(input(f"Enter marks of subject {j+1} for student {i+1}: "))
#     percent = marks / 5
#     print(f"Percentage of student {i+1}: {percent}%")
#     total_percent += percent

# print("Average Percentage:", total_percent / students)

#while  loop
students = int(input("Enter number of students: "))
i, total_percent = 0, 0

while i < students:
    marks, j = 0, 0
    while j < 5:
        marks += int(input(f"Enter marks of subject {j+1} for student {i+1}: "))
        j += 1
    percent = marks / 5
    print(f"Percentage of student {i+1}: {percent}%")
    total_percent += percent
    i += 1

print("Average Percentage:", total_percent / students)

