# Write a Python program to find the two numbers whose product is 
# maximum among all the pairs in a given list of numbers. Use the 
# Python set.

numbers = [1, 4, 3, 6, -2, -8, 0, 6]
numbers = list(set(numbers))
max1 = max(numbers)
numbers.remove(max1)
max2 = max(numbers)
min1 = min(numbers)
numbers.remove(min1)
min2 = min(numbers)
if max1 * max2 > min1 * min2:
    pair = (max1, max2)
    max_product = max1 * max2
else:
    pair = (min1, min2)
    max_product = min1 * min2
print("Pair with maximum product:", pair)
print("Maximum product:", max_product)
