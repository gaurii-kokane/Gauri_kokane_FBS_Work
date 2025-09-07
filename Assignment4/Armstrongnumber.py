# start, end = 100, 999
# for num in range(start, end+1):
#     s = sum(int(d)**3 for d in str(num))
#     if s == num:
#         print(num, end=" ")
        
# Program to find Armstrong numbers within a given range using for loop

# Taking input from user
# lower = int(input("Enter lower range: "))
# upper = int(input("Enter upper range: "))

# print(f"Armstrong numbers between {lower} and {upper} are:")

# for num in range(lower, upper + 1):
#     # Calculate the number of digits
#     power = len(str(num))
#     temp = num
#     sum_of_powers = 0

#     # Find sum of digits raised to the power
#     while temp > 0:
#         digit = temp % 10
#         sum_of_powers += digit ** power
#         temp //= 10

#     # Check if it is an Armstrong number
#     if num == sum_of_powers:
#         print(num)
# Simple Armstrong number program in a given range

# start = int(input("Enter start: "))
# end = int(input("Enter end: "))

# print("Armstrong numbers are:")

# for num in range(start, end + 1):
#     s = 0
#     for d in str(num):  # loop through digits
#         s += int(d) ** len(str(num))
#     if s == num:
#         print(num)
# Simple Armstrong number program in a given range

start = int(input("Enter start: "))
end = int(input("Enter end: "))

print("Armstrong numbers are:")

for num in range(start, end + 1):
    s = 0
    for d in str(num):  # loop through digits
        s += int(d) ** len(str(num))
    if s == num:
        print(num)
