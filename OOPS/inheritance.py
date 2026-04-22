#parent class
class Vehicle:
    def vehicle_info(self):
        print("inside vehicle class")

#child class
class Car(Vehicle):
    def car_info(self):
        print("inside car class")


#creating object of child class
c1=Car()
#access vehicles info using car object
c1.vehicle_info()
c1.car_info()