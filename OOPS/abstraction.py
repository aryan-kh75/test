#Abstraction is a process of hiding the implementation details and showing only functionality to the user.
#In OOPs, abstraction can be achieved using abstract classes and interfaces.
#An abstract class is a class that cannot be instantiated and is typically used as a base class for other classes.
#It can contain abstract methods, which are methods that are declared but not implemented in the abstract class.
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