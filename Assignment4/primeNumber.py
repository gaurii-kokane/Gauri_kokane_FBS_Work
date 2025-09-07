num=int(input("Enter Number:"))
for i in  range(2,num):
    if(num%i==0):
        print(f'{num} is Not Prime')
        break
else:
    print(f'{num}Is Prime')

#while  loop
n = int(input("Enter number: "))
i, is_prime = 2, True
while i <= int(n**0.5):
    if n % i == 0:
        is_prime = False
        break
    i += 1
print("Prime" if is_prime and n > 1 else "Not Prime")
    