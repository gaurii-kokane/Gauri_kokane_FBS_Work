#Write a program to find maximum and minimum element in a list.

numbers = [5, 10, 15, 20] 
maxi = numbers[0] 
mini = numbers[0]
for n in numbers: 
  if n > maxi:
   maxi = n 
   if n < mini: 
    mini = n 
print("Max =", maxi)     
print("Min =", mini)