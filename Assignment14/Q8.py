# Write a Python program to find all the anagrams and group them 
# together from a given list of strings.

from collections import defaultdict
words = ["eat", "tea", "tan", "ate", "nat", "bat"]
anagrams = defaultdict(list)

for word in words:
    key = tuple(sorted(word))
    anagrams[key].append(word)
print("Grouped Anagrams:")
for group in anagrams.values():
    print(group)
