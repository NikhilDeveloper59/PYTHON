# Hiding internal implementation & showing required details.    
# Python uses ABC module:
#     ABC → Abstract Base Class
#     @abstractmethod → abstract method (must be implemented in child class)

from abc import ABC , abstractmethod

class Vehicle(ABC): # abstract class

    @abstractmethod
    def start(self):  # abstract method
        pass

class Bike(Vehicle):
    def start(self):
        print("Bike starts with kick")

class Car(Vehicle):
    def start(self):
        print("Car starts with key")


print(Bike.start())
print(Car.start())

# Rule1:You cannot create object of abstract class like v = Vehicle()  # ❌ Error
# Rule 2:Child class must implement all abstract methods,Otherwise child also becomes abstract.
