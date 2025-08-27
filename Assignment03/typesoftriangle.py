# 5. Type of triangle
a = int(input("Enter side1: "))
b = int(input("Enter side2: "))
c = int(input("Enter side3: "))
if a==b==c:
    print("Equilateral Triangle")
elif a==b or b==c or a==c:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")
