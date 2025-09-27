# Accept a number from user and check if this element is present in the list or 
# not. Also tell how many times it is present in the list.



numbers = [5, 10, 15, 20, 10, 5, 10]

element = int(input("Enter a number: "))

count = 0
for n in numbers:
    if n == element:
        count += 1

if count > 0:
    print(element, "is present", count, "time(s)")
else:
    print(element, "is NOT present in the list")
