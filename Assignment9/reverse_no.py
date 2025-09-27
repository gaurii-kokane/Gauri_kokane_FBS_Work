#Write a program to reverse a given number using recursive function.
def reverseNumber(n, rev=0):
    if n == 0:   
        return rev
    else:
        return reverseNumber(n // 10, rev * 10 + n % 10)
n = int(input("Enter number: "))
print("Reversed number:", reverseNumber(n))



