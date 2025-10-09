from  abc import ABC,abstractmethod
class Vehicle(ABC):
    def __init__(self,persons):
        self.perons=persons
    @abstractmethod    
    def calculate_Toll(self):
        pass
class Twowheeler(Vehicle):
    def __init__(self,persons) :
        super().__init__(persons) 
        self.base_toll=20
        self.extra_charge=10
        self.max_persons=2
    def calculate_Toll(self):
        toll=self.base_toll
        if  self.persons>self.max_persons:
            toll+=(self.persons-self.max_persons)+self.extra_charge
        return  toll    
class Threewheeler(Vehicle):
    def __init__(self,persons) :
        super().__init__(persons) 
        self.base_toll=30
        self.extra_charge=20
        self.max_persons=3
    def calculate_Toll(self):
        toll=self.base_toll
        if  self.persons>self.max_persons:
            toll+=(self.persons-self.max_persons)+self.extra_charge
        return  toll    
class Fourwheeler(Vehicle):
    def __init__(self,persons) :
        super().__init__(persons) 
        self.base_toll=40
        self.extra_charge=40
        self.max_persons=4
    def calculate_Toll(self):
        toll=self.base_toll
        if  self.persons>self.max_persons:
            toll+=(self.persons-self.max_persons)+self.extra_charge
        return  toll  
class heavywheeler(Vehicle):
    def __init__(self,persons) :
        super().__init__(persons) 
        self.base_toll=60
        self.extra_charge=100
        self.max_persons=6
    def calculate_Toll(self):
        toll=self.base_toll
        if  self.persons>self.max_persons:
            toll+=(self.persons-self.max_persons)+self.extra_charge
        return  toll   
def main():
    while True:
        print('\nToll calculation :')   
        print("1.Twowheeler:")
        print("2.Threewheeler:")
        print("3.fourwheeler:")
        print("4.Heavywheeler:")
        print("5.Exit")

        choice=input("enter your choice")

        if  choice  in['1','2','3','4']:
            persons=int(input("enter the number of  persons:"))
            if  choice=='1':
                Vehicle=Twowheeler(persons) 
            elif choice=='2': 
                Vehicle=Threewheeler(persons)   
            elif choice=='3': 
                Vehicle=Fourwheeler(persons) 
            else:
                Vehicle=heavywheeler(persons) 
            toll=Vehicle.calculate_Toll()  
            print(f"Toll amount:")
        elif choice=='5':
            print("existing program")
            break
        else:
            print("Invalid  choice")
if  __name__=='__main__':
    main()


        
        

