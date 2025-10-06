#Create a class Book with members as bid,bname,price and author.Add following  methods:  
# a. Constructor (Support both parameterized and parameterless)  
# b. Destructor   
# c. ShowBook

class Book:
    def __init__(self, bid, bname, price, author):
        self.bid = bid
        self.bname = bname
        self.price = price
        self.author = author
        print("Book object is created.")

    def showBook(self):
        return f'ID:{self.bid}\nNAME:{self.bname}\nPRICE:{self.price}\nAUTHOR:{self.author}'

    def __del__(self):
        print("Book object deleted.")

b1 = Book(101, "Python Basics", 450, "Guido van Rossum")
print(b1.showBook())
print()

