#
list_of_sublists = [[1, 3], [3, 1], [5, 2]]
def get_second(sublist):
    return sublist[1]
sorted_list = sorted(list_of_sublists, key=get_second)
print(sorted_list)
