# Create a class Product with members as pid,pname,price and quantity .Add 
# following methods:  
# d. Constructor (Support both parameterized and parameterless)  
# e. Destructor   
# f. ShowBook 

class Product:
    def __init__(self, pid, pname, price, quantity):
        self.pid = pid
        self.pname = pname
        self.price = price
        self.quantity = quantity
        print("product is created")

    def showProduct(self):
        return f'ID:{self.pid}\nNAME:{self.pname}\nPRICE:{self.price}\nQUANTITY:{self.quantity}'

    def __del__(self):
        print("Product object deleted.")

p1 = Product(201, "Laptop", 55000, 10)
print(p1.showProduct())
print()
