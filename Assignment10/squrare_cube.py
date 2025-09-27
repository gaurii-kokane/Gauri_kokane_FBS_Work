#Write a program to create three lists of numbers, their squares and  cubes

# Program to create three lists: numbers, squares, and cubes (without using inbuilt methods)

numbers = [1,2,3,4,5]  
squares = [0] *5
cubes = [0] *5

for i in range(5):
    numbers[i] = i + 1
    squares[i] = (i + 1) ** 2
    cubes[i] = (i + 1) ** 3

print("Numbers:", numbers)
print("Squares:", squares)
print("Cubes:", cubes)
