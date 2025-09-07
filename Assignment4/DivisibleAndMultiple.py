# Find numbers divisible by 7 and multiple of 5 in a given range
start, end = 1, 100
for i in range(start, end+1):
    if i % 7 == 0 and i % 5 == 0:
        print(i, end=" ")
print()        

#While  loop
start, end = 1, 200
i = start
while i <= end:
    if i % 7 == 0 and i % 5 == 0:
        print(i, end=" ")
    i += 1
        



