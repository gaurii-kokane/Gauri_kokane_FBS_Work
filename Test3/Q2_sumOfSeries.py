#write  program to calculate  the sum of  series  of  following  
#1/1!+2/2!+3/3!+.....N/N!

N = int(input("Enter the value of N: "))
sum_series = 0
fact = 1
for i in range(1, N + 1):
    fact *= i        
    sum_series += i / fact
print("Sum of series:", sum_series)

