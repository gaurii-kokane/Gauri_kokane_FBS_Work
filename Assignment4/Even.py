# 1. Print all even numbers until n forloop
# n = int(input("Enter n: "))
# for i in range(2, n+1, 2):
#     print(i, end=" ")
# print()

#use whileloop


n = int(input("Enter n: "))
i = 2
while i <= n:
    print(i, end=" ")
    i += 2

