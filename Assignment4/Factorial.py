# 4. Factorial of a number
n = int(input("Enter number: "))
fact = 1
for i in range(1, n+1):
    fact *= i
print("Factorial =", fact)
print()

#while  loop
n = int(input("Enter n: "))
fact, i = 1, 1
while i <= n:
    fact *= i
    i += 1
print("Factorial =", fact)
