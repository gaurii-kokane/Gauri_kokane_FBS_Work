# 3. Sum of series up to n
n = int(input("Enter n: "))
s = 0
for i in range(1, n+1):
    s += i
print("Sum =", s)
print()

#while  loop
n = int(input("Enter n: "))
s, i = 0, 1
while i <= n:
    s += i
    i += 1
print("Sum =", s)



