#WAP to print following patterns :
# #Print the top horizontal line(Z)
for i in range(19):
    print("*", end="")
print()

for i in range(7):
    for j in range(19 - 1 - i):  
        print(" ", end="")
    print("*")  

for i in range(19-1):
    print("*", end="")
print()
