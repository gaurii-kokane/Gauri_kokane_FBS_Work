length = float(input("Enter length of room: "))
breadth = float(input("Enter breadth of room: "))
height = float(input("Enter height of room: "))
rate = float(input("Enter painting cost per sq.m: "))

area = 2 * height * (length + breadth)
cost = area * rate

if cost > 0:
    print("Total painting cost = Rs.", cost)
else:
    print("Invalid input, please check dimensions")
