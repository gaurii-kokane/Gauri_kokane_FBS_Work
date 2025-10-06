#Python Program to Find the Second Largest Number in a List Using Bubble sort

# def bubbleSort(li):
#     n = len(li)
#     for i in range(n):
#         for j in range(0, n-i-1): 
#             if li[j] > li[j+1]:
#                 li[j], li[j+1] = li[j+1], li[j]
#                 print(li)  
#     return li

# li = [60, 50, 40, 30, 20, 10]
# print("Original List:", li)
# li = bubbleSort(li)
# print("Sorted List:", li)


# List of numbers
numbers = [5, 2, 9, 1, 7]

# Bubble Sort to sort the list in ascending order
n = len(numbers)
for i in range(n):
    for j in range(0, n-i-1):
        if numbers[j] > numbers[j+1]:
            # Swap if current element is greater than next
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

# The second largest number is the second last element
second_largest = numbers[-2]

print("Second Largest Number:", second_largest)
