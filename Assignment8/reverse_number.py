# Write a program find reverse of a number 
# Program 8: Reverse of a number using Function

def reverseNumber(num):
    num = num
    rev = 0
    while num > 0:
        rev = rev * 10 + num % 10
        num //= 10
    return  rev
num = int(input("Enter a number: "))
print("Reverse of Number =", reverseNumber(num))

