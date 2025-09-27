#1. Write a program to find sum of following series using recursive functions:
# 1! + 2! + 3! + 4! +..... + n!

def fact(n):
    if n == 0 :
        return 1
    return n * fact(n - 1)
def sumofFact(n):
    if n == 0:
        return 0
    return fact(n) + sumofFact(n - 1)
n = int(input("Enter n:"))
print("Sum of series:", sumofFact(n))
