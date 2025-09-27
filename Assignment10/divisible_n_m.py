#Write a program to print all numbers which are divisible by m and n in list


start = 1
end = 50
m = 3
n = 5

result = []
for i in range(start, end + 1):
    if i % m == 0 and i % n == 0:
        result.append(i)

print(result)
