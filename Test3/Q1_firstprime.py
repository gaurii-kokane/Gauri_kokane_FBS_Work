#write  program to  print   first   n   prime   numbers
n=int(input("Enter  the number:"))
count,num=0,2
while   count<n:
    for i   in  range(2,num//2+1):
        if(num%i==0):
            break
    else:
        print(num,end=' ')  
        count+=1
    num+=1          
        