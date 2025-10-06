#  Python Program to count the occurrences of each word in a string. 


text = "hello world hello python"
words = text.split()
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print(word_count)

