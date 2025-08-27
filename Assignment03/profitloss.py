
# calculate Profit or Loss
cp = float(input("Enter cost price: "))
sp = float(input("Enter selling price: "))
if sp > cp:
    print("Profit =", sp-cp)
elif sp < cp:
    print("Loss =", cp-sp)

