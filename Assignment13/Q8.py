#Python Program to Count the Frequency of Words Appearing in a String Using 
# a Dictionary

text = input("Enter a string: ")
words = text.split()
freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1
print("Word Frequency:", freq)
