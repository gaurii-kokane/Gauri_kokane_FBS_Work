#Write a program to remove all occurrences of a given element in the list.

numbers = [1, 2, 3, 2, 4, 2, 5]
x = 2 
new_list = []
for num in numbers:
    if num != x:
        new_list.append(num)

print(new_list)
