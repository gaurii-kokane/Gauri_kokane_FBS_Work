#Write a program to check if entered year is a leap year or not.
def leapYear(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
year = int(input("Enter a year: "))
if leapYear(year):
    print(year, "is a Leap Year.")
else:
    print(year, "is not a Leap Year.")
