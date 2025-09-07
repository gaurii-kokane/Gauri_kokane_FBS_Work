n = int(input("Enter number: "))
p = len(str(n))
s = sum(int(d)**p 
        for d in str(n))
print("Armstrong" if s == n
       else "Not Armstrong")

#While  loop
n = int(input("Enter number: "))
temp, p, s = n, len(str(n)), 0
while temp > 0:
    d = temp % 10
    s += d ** p
    temp //= 10
print("Armstrong" if s == n else "Not Armstrong")
