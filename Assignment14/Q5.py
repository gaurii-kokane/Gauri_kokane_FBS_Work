#  Write a Python program to find the longest common prefix of all strings. Use the Python set. 

strings = ["flower", "flow", "flight"]
prefix = strings[0]
for s in strings[1:]:
    while prefix and prefix != s[:len(prefix)]:
        prefix = prefix[:-1]  
print("Longest common prefix:", prefix)
