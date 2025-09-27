#Write a program to find sum of digits using recursion.

def sumofDigits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sumofDigits(n // 10)

n = int(input("Enter number: "))
print("Sum of digits:", sumofDigits(n))

