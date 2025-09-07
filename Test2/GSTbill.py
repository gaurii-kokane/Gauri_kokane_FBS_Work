
# Accept 5 products individually
p1 = float(input("Enter price of product 1: "))
p2 = float(input("Enter price of product 2: "))
p3 = float(input("Enter price of product 3: "))
p4 = float(input("Enter price of product 4: "))
p5 = float(input("Enter price of product 5: "))

total = p1 + p2 + p3 + p4 + p5

if total > 0:
    gst = total * 0.18
    final_bill = total + gst
    print("Total bill after 18% GST = Rs.", round(final_bill, 2))
else:
    print("No valid products entered")
