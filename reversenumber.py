#revesrenumber
num=int(input("enter the number:"))
d1=num//100
d2=(num//10)%10
d3=num%10
reverse=d3*100+d2*10+d1
print("reversed number:",reverse)