# 8. Captcha-like program
import random
userid = input("Enter userid: ")
password = input("Enter password: ")
if userid == "admin" and password == "1234":
    num = random.randint(1000,9999)
    print("Enter this number:", num)
    ans = int(input("Re-enter number: "))
    if ans == num:
        print("Login Successful")
    else:
        print("Captcha Failed")
else:
    print("Invalid Credentials")

