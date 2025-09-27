#Write a program to find sum of following series using functions : 
#a.  1+ 2 + 3 + 4+….. + n 
#b. 1!+ 2! + 3! + 4!+….. + n! 
#c. 1^1 + 2^2 + 3^3+ …… n^n

#a
def sum(n):
    total=0
    for i in range(1,n+1):
        total+=i
    return  total
n=int(input("Enter n terms: "))
print("sum:",sum(n))  


#b
# Program 3b: Sum of factorial series using Function

def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return fact
def factorialSeries(n):
    total = 0
    for i in range(1, n + 1):
        total += factorial(i)
    return total
n = int(input("Enter value of n: "))
print("Sum of Factorial Series =", factorialSeries(n))

#c
#  Sum of power 

def powerSeries(n):
    total = 0
    for i in range(1, n + 1):
        power = 1
        for j in range(i):
            power *= i
        total += power
    return total
n = int(input("Enter value of n: "))
print("Sum of Power Series =", powerSeries(n))


