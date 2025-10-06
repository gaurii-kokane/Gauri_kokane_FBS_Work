# Python Program to Remove the nth Index Character from a Non-Empty String

text = "HelloWorld"
n = 4 
new_text = text[:n] + text[n+1:]
print(new_text)
