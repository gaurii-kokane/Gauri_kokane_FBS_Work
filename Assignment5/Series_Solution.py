#a. 1! + 2! + 3! + 4! + …..n!
# import  math
# n = int(input("Enter n: "))
# s = 0
# for i in range(1, n+1):
#     s +=math.factorial(i)
# print("Sum =", s)

#b. N + N^2 + N^3+N^4 …..+N^N (here ^ means exponent)
# N = int(input("Enter N: "))
# s = 0
# for i in range(1, N+1):
#     s += N ** i
# print("Sum =", s)

#c. Find the sum of a geometric series from 1 to n where the common ratio is 2.
# n = int(input("Enter n: "))
# s, term = 0, 1
# for i in range(n):
#     s += term
#     term *= 2
# print("Sum =", s)

#d. S = a + a2 / 2 + a3 / 3 + …… + a10 / 10
a = int(input("Enter a: "))
s = 0
for i in range(1, 11):
    s += (a ** i) / i
print("Sum =", s)

#e.x - x2/3 + x3/5 - x4/7 + …. to n terms 
x = int(input("Enter x: "))
n = int(input("Enter terms: "))
s = 0
sign = 1
for i in range(1, n+1):
    s += sign * (x ** i) / (2*i - 1)
    sign *= -1
print("Sum =", s)





