#10. Write a program to reverse a number using recursion. 

def reverse_number(n, rev=0):
    if n == 0:
        return rev
    else:
        return reverse_number(n // 10, rev * 10 + n % 10)

n = int(input("Enter number: "))
print("Reversed number:", reverse_number(n))
