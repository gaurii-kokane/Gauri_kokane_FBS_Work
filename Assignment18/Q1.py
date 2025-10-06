# Create a class Complex Number with data members as real and imag and add 
# following methods : 
# a. Constructor 
# b. Destructor 
# c. Overload +,-  operator

class ComplexNumber:
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag
        print("Constructor called")

    def __del__(self):
        print("Destructor called for ComplexNumber")

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imag - other.imag)

    def __str__(self):
        return f"{self.real} + {self.imag}i"

c1 = ComplexNumber(5, 3)
c2 = ComplexNumber(2, 4)

print("Addition:", c1 + c2)
print("Subtraction:", c1 - c2)
