#Python Program to Remove the Given Key from a Dictionary


my_dict = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
key = input("Enter the key to remove: ")
if key in my_dict:
    my_dict.pop(key)
    print(f"Key '{key}' removed successfully.")
else:
    print(f"Key '{key}' not found in the dictionary.")

print("Updated dictionary:", my_dict)
