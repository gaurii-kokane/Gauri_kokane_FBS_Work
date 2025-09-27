#write a program to find the second largest element in the list.

numbers = [5, 10, 15, 20]
largest = numbers[0]
second = numbers[0]
for n in numbers:
    if n > largest:
        second = largest 
        largest = n
    elif n > second and n != largest:
        second = n
print("Second Largest =", second)
