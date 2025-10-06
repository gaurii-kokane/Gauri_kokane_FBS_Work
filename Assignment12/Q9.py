#Python Program to Calculate the Number of Words and the Number of 
#Characters Present in a String 


text = "Hello World Python"
num_chars = len(text.replace(" ", ""))
num_words = len(text.split())

print("Number of characters (excluding spaces):", num_chars)
print("Number of words:", num_words)

