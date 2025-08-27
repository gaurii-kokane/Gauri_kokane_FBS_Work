a = int(input("Enter coefficient a: "))
b = int(input("Enter coefficient b: "))
c = int(input("Enter coefficient c: "))
d = b*b - 4*a*c
root1 = (-b + d**0.5) / (2*a)
root2 = (-b - d**0.5) / (2*a)
print("Root1 =", root1)
print("Root2 =", root2)

