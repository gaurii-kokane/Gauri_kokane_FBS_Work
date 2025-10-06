#  Create a class Shirt  with members as sid,sname,type(formal etc), price and 
# size(small,large etc) .Add following methods:  
# j. 
# Constructor (Support both parameterized and parameterless)  
# k. Destructor   
# l. 
# ShowBook  
# m. For each size of shirt price should change by 10%. 
# (eg. If 1000 is price then small price = 1000, medium = 1100,large=1200 and 
# xlarge=1300) Use static concept.

class Shirt:
    size_price = {
        "S": 0,   
        "M": 10,   
        "L": 20,   
        "XL": 30 
    }

    def __init__(self, sid=0, sname="Unknown", stype="Casual", price=0.0, size="S"):
        self.sid = sid
        self.sname = sname
        self.stype = stype
        self.price = price
        self.size = size.upper()
        print("Shirt object created.")

    def showShirt(self):
        increment = Shirt.size_price.get(self.size, 0)
        final_price = self.price + (self.price * increment / 100)
        return (f'ID: {self.sid}\n'
                f'NAME: {self.sname}\n'
                f'TYPE: {self.stype}\n'
                f'BASE PRICE: {self.price}\n'
                f'SIZE: {self.size}\n'
                f'FINAL PRICE: {final_price}')

    def __del__(self):
        print("Shirt object deleted.")

s1 = Shirt(301, "Raymond", "Formal", 1000, "S")
print(s1.showShirt())
print()

s2 = Shirt(302, "Peter England", "Casual", 1000, "M")
print(s2.showShirt())
print()

s3 = Shirt(303, "Arrow", "Formal", 1000, "L")
print(s3.showShirt())
print()

s4 = Shirt(304, "Van Heusen", "Partywear", 1000, "XL")
print(s4.showShirt())
