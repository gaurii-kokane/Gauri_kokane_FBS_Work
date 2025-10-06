# Given two sets of numbers, write a Python program to find the missing 
# numbers in the second set as compared to the first and vice versa. 
# Use the Python set.

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7}
missing_numbers = set1.symmetric_difference(set2)

print("Numbers missing in either set:", missing_numbers)
