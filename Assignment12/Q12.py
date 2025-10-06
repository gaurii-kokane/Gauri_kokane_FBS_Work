#.  Python Program to count number of lowercase characters in a string. 

text = "Hello World Python"
count = 0
for char in text:
    if 'a' <= char <= 'z':
        count += 1
print("Lowercase letters:", count)
