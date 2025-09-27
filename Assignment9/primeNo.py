#Write a program to check whether a number is prime or not using recursion.

def prime(n, i=2):
    if n <= 1:
        return False
    if i * i > n:
        return True
    if n % i == 0:
        return False
    return prime(n, i + 1)

n = int(input("Enter number: "))
print(f"{n} is prime" if prime(n) else f"{n} is not prime")
