#Python Program to Sort a List According to the Length of the Elements 
# within the list.

lists = [[1,2,3], [4,5], [6,7,8,9], [10]]
lists.sort(key=len)
print(lists)
