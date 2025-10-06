# Create a class Shirt  with members as sid,sname,type(formal etc), price and 
# size(small,large etc) .Add following methods:    
# g. Constructor (Support both parameterized and parameterless)  
# h. Destructor  
# i.showBook

class Shirt:
    def __init__(self, sid, sname, stype, price, size):
        self.sid = sid
        self.sname = sname
        self.stype = stype
        self.price = price
        self.size = size
        print("Shirt is created")

    def showShirt(self):
        return f'ID:{self.sid}\nNAME:{self.sname}\nTYPE:{self.stype}\nPRICE:{self.price}\nSIZE:{self.size}'

    def __del__(self):
        print("Shirt object deleted.")

s1 = Shirt(301, "Raymond", "Formal", 1200, "L")
print(s1.showShirt())
print()
