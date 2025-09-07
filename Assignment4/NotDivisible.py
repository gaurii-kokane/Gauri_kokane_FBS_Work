
# Print all integers upto n not divisible by 2 and 3
n = int(input("Enter n: "))
for i in range(1, n+1):
    if i % 2 != 0 and i % 3 != 0:
        print(i, end=" ")
print()

#While  loop
n = int(input("Enter n: "))
i = 1
while i <= n:
    if i % 2 != 0 and i % 3 != 0:
        print(i, end=" ")
    i += 1

