# for i in range(1, 10):
#     print("* " * i)

for i in range(1, 10, 2):         # 9 → 7 → 5 → 3 → 1
    spaces = (1- i) // 2         # calculate spaces to center stars
    print(" " * spaces + "* " * i)

