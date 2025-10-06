# Create a class Book with members as bid,bname,price and author.Add following 
# methods:  
# a. Constructor (Support both parameterized and parameterless)  
# b. Destructor   
# c. ShowBook  
# d. Add static variable count and also maintain count of objects created.

class Book:
    count = 0
    def __init__(self, bid, bname, price, author):
        self.bid = bid
        self.bname = bname
        self.price = price
        self.author = author
        Book.count += 1
        print("Book object created.")

    def showBook(self):
        return f'ID:{self.bid}\nNAME:{self.bname}\nPRICE:{self.price}\nAUTHOR:{self.author}\nTOTAL OBJECTS:{Book.count}'

    def __del__(self):
        print("Book object deleted.")

# Example
b1 = Book(101, "Python Basics", 450, "Guido van Rossum")
print(b1.showBook())
b2 = Book(102, "Data Science", 600, "Wes McKinney")
print(b2.showBook())
