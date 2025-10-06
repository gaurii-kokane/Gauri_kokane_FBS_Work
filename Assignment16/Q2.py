# Create a class Product with members as pid,pname,price and quantity .Add 
# following methods:  
# e. Constructor (Support both parameterized and parameterless)  
# f. Destructor   
# g. ShowBook  
# h. Add static member discount.  
# i. Provide methods for applying discount on price of product. 

class Product:
    # static member
    discount = 0  

    def __init__(self, pid, pname, price, quantity):
        self.pid = pid
        self.pname = pname
        self.price = price
        self.quantity = quantity
        print("Product object created.")

    def showProduct(self):
        final_price = self.price - (self.price * Product.discount / 100)
        return (f'ID: {self.pid}\n'
                f'NAME: {self.pname}\n'
                f'ORIGINAL PRICE: {self.price}\n'
                f'DISCOUNT: {Product.discount}%\n'
                f'FINAL PRICE: {final_price}\n'
                f'QUANTITY: {self.quantity}')

    @staticmethod
    def applyDiscount(percent):
        Product.discount = percent
    def __del__(self):
        print("Product object deleted.")
p1 = Product(101, "Laptop", 55000, 5)
p2 = Product(102, "Mobile", 25000, 10)
Product.applyDiscount(10)
print(p1.showProduct())
print()
print(p2.showProduct())
