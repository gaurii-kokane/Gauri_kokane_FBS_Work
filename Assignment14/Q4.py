# Write a Python program that finds all pairs of elements in a list whose 
# sum is equal to a given value

numbers = [1, 2, 3, 4, 5, 6, 7]
target_sum = 7
print("Pairs with sum", target_sum, ":")
for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        if numbers[i] + numbers[j] == target_sum:
            print((numbers[i], numbers[j]))
