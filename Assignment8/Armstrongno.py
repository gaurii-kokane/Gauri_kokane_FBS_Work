def checkArmstrong(num):
    original_num = num
    temp = num
    digits = 0
    while temp > 0:
        digits += 1
        temp //= 10
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** digits
        temp //= 10
    if num == sum:
        print("Armstrong Number")
    else:
        print("Not Armstrong Number")
num = int(input("Enter a number: "))
checkArmstrong(num)

