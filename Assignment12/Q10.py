# Python Program to Take in Two Strings and Display the Larger String 
# without Using Built-in Functions

str1 = "Gaurii"
str2 = "firstbitsolution"
count1 = 0
for c in str1:
    count1 += 1
count2 = 0
for c in str2:
    count2 += 1
if count1 > count2:
    print(str1)
elif count2 > count1:
    print(str2)
else:
    print("Both strings are equal")
