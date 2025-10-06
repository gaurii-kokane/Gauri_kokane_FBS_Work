# Python Program to Count the Number of Vowels in a String
text = "Firstbit solution"
vowels = "aeiouAEIOU"
count = 0
for char in text:
    if char in vowels:
        count += 1
print("Number of vowels:", count)
