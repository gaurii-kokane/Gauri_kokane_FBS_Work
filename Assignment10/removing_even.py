 #Write a program to print list after removing even numbers. 

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

result = []
for n in numbers:
    if n % 2 != 0: 
        result.append(n)

print(result)
