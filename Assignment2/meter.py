#conver feet and inches in meter and cm
feet=float(input("Enter feet:"))
inches=float(input("Enter inches:"))
cm=(feet+30.48)+(inches+2.54)
meter=cm/100
print("Meter is :",meter)
print("centimeter is:",cm)