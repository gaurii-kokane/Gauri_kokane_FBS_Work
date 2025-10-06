#Python Program to Concatenate Two Dictionaries Into One 

# Define two dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

result = dict1.copy()

result.update(dict2)

print("Concatenated Dictionary:", result)
