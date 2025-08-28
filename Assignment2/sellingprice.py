#calculate seeling price of book base on cost and discount
cp=float(input("Enter the cost price of book:"))
Discount=float(input("Enter the Discount price on book:"))
sp=cp-(cp*Discount/100)
print("Selling price of based on cost and discount is :",sp)