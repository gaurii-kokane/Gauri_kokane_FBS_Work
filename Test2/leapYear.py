# Program to check if a year is a Leap Year

year = int(input("Enter a year: "))

if year % 4 == 0:  # divisible by 4
    if year % 100 == 0:  # divisible by 100
        if year % 400 == 0:  # divisible by 400
            print(year, "is a Leap Year")
        else:
            print(year, "is NOT a Leap Year")
    else:
        print(year, "is a Leap Year")
else:
    print(year, "is NOT a Leap Year")
