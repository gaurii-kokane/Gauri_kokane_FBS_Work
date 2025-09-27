#Write a program to print Fibonacci series using recursion.

def fibonacci(n,a,b):
    if(n>0):
        c=a+b
        print(c,end=" ")
        fibonacci(n-1,b,c)
n=int(input("enter number:"))        
fibonacci(n,-1,1)
