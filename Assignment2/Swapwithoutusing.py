#swap without using third variable
a=int(input("enter number:"))
b=int(input("enter number:"))
a=a+b
b=a-b
a=a-b
print("Afterswap:a=",a,",b=",b)
