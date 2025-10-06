#Python Program to count number of digits and letters in a string. 

text = "Hello123 World45"
letters = 0
digits = 0
for char in text:
    if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
        letters += 1
    elif '0' <= char <= '9':
        digits += 1
print("Letters:", letters)
print("Digits:", digits)
