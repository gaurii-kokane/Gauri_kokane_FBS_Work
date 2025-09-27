# Write a program to find sum of digits of a number

def sum_of_digits(num):
    num = num
    total = 0
    while num > 0:
        total += num % 10
        num //= 10
    return total

num = int(input("Enter a number: "))
print("Sum of Digits =", sum_of_digits(num))
