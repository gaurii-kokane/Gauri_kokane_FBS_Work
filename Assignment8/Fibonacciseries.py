#write  program to  find print the following fibonacci series using functions
#1 1 2 3 5 8 n terms 
def fibonacciSeries(n):
    a = -1
    b=1
    print("Fibonacci Series:")
    for i in range(n):
        c=a+b
        print(c, end=" ")
        a=b
        b=c
n = int(input("Enter number of terms: "))
fibonacciSeries(n)
