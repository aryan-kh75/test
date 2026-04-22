from abc import ABC, abstractmethod
class Car(ABC):
    @abstractmethod
    def mileage(self):
        pass

class defender(Car):
    def mileage(self):
        print("mileage is 7km/l")

class fortuner(Car):
    def mileage(self):
        print("mileage is 10km/l")

class pajero(Car):
    def mileage(self):
        print("mileage is 8km/l")


d=defender()
d.mileage()

i=fortuner()
i.mileage()

p=pajero()
p.mileage()