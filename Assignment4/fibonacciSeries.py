# 5. Fibonacci series up to n terms
# n = int(input("Enter n terms: "))
# a=-1
# b=1
# for i in range(n):
#     c=a+b
#     print(c)
#     a=b
#     b=c

#While  loop
n = int(input("Enter number of terms: "))
a, b, i = 0, 1, 0
while i < n:
    print(a, end=" ")
    a, b = b, a+b
    i += 1
    

