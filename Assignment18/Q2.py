#Create a class Distance with data members as km,m and cm and add following 
# methods : 
# a. Constructor 
# b. Destructor 
# c. Overload +,-  operator

class Distance:
    def __init__(self, km=0, m=0, cm=0):
        self.km = km
        self.m = m
        self.cm = cm
        print("Constructor called")

    def __del__(self):
        print("Destructor called for Distance")

    def __add__(self, other):
        total_cm = (self.km + other.km) * 100000 + (self.m + other.m) * 100 + (self.cm + other.cm)
        km = total_cm // 100000
        m = (total_cm % 100000) // 100
        cm = total_cm % 100
        return Distance(km, m, cm)

    def __sub__(self, other):
        total_cm1 = self.km * 100000 + self.m * 100 + self.cm
        total_cm2 = other.km * 100000 + other.m * 100 + other.cm
        diff = abs(total_cm1 - total_cm2)
        km = diff // 100000
        m = (diff % 100000) // 100
        cm = diff % 100
        return Distance(km, m, cm)

    def __str__(self):
        return f"{self.km} km, {self.m} m, {self.cm} cm"
d1 = Distance(2, 350, 75)
d2 = Distance(1, 800, 50)

print("Addition:", d1 + d2)
print("Subtraction:", d1 - d2)
