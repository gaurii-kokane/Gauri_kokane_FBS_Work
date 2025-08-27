p = float(input("Enter Principal: "))
t = float(input("Enter Time: "))
r = float(input("Enter Rate: "))
ci = p * (pow((1 + r / 100), t)) - p
print("Compound Interest =", ci)