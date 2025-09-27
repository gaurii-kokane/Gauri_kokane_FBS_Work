#Write a program to create a new list from existing list which contains cube of 
# each number of list.

numbers = [1,2,3,4,5,6] 
cubes = [] 
for n in numbers:
 cubes.append(n*n*n) 
 print("Cubes:", cubes)