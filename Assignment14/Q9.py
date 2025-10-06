# Write a Python program to find all the unique combinations of 3 
# numbers from a given list of numbers, adding up to a target number.

from itertools import combinations

# Given list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7]
target = 12
comb = combinations(numbers, 3)
result = [c for c in comb if sum(c) == target]

print("Combinations of 3 numbers that sum to", target, ":")
for r in result:
    print(r)

