# Check Perfect Number
n = int(input("Enter number: "))
s = 0
for i in range(1, n):
    if n % i == 0:
        s += i
print(n, "is Perfect")

#While  loop
n = int(input("Enter number: "))
i, s = 1, 0
while i < n:
    if n % i == 0:
        s += i
    i += 1
print("Perfect" if s == n else "Not Perfect")


