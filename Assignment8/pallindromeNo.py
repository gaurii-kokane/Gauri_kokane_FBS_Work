#write  program to  check   if  entered number  is  pallindrome or  not
def checkPalindrome(num):
    original_num = num
    reversed_num = 0
    while num > 0:
        digit = num % 10
        reversed_num = (reversed_num * 10) + digit
        num //= 10
    if original_num == reversed_num:
        print("Palindrome")
    else:
        print("Not Palindrome")
num = int(input("Enter a 3-digit number: "))
checkPalindrome(num)
