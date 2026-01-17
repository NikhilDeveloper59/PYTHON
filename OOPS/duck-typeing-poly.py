# Duck Typing:
# Python doesn’t care about class type, only checks behavior.
# If it walks like a duck and quacks like a duck → it is a duck ✅

class Bike:
    def start(self):
        print("Bike is started")

class Car:
    def start(self):
        print("Car is started")


def running(vehicle):
    vehicle.start()

b = Bike()
c = Car()
running(b)
running(c)
      