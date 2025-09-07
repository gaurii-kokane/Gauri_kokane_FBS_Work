for i in range(5, 0, -1):              
    for j in range(1, 6):
        if i == 5   or j == 1 or i == j:
            print(j, end="  ")
        else:
            print(" ", end="  ")
    print()
for i in range(5, 0, -1):           # Rows 5 → 1
    for j in range(1, 6):           # Columns 1 → 5
        if i == 5 or j == 1 or i == j:
            print(j, end="  ")
        else:
            print(" ", end="  ")
    print()
