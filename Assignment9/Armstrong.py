#Write a program to check if given number is Armstrong or not using recursive
def digit_cnt(num):
    cnt=0
    while(num!=0):
        num=num//10
        cnt+=1
    return  cnt    
def sum_of_pow(num,cnt):
    sum=0
    while(num!=0):
        rem=num%10
        sum=sum+(rem**cnt)
        num=num//10
    return  sum
def armstrong(num):  #calling  function
    cnt=digit_cnt(num)      #called function
    sum=sum_of_pow(num,cnt)
    if  sum==num:
        print(num,"is Armstrong!!")
    else:
        print(num,"is not Armstrong") 

num=int(input("Enter the number:"))
armstrong(num)    
