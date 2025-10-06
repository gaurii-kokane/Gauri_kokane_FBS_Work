#Write a Python program to find all the unique words and count the frequency of occurrence from a given list of strings. Use Python set data type.

# Given list of strings
lines = ["Python is fun", "Python is easy", "Python is powerful"]
words = []
for line in lines:
    words.extend(line.split())
unique_words = set(words)
for word in unique_words:
    print(word, ":", words.count(word))
