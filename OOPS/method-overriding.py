# Method Overriding (Run-Time Polymorphism)
# Same method in parent + child class, child version runs.

class Animal:
    def sound(self):
         print("Animal makes sound")

class Dog(Animal):
     def sound(self):
          print("Dog barks")

class Cat(Animal):
     def sound(self):
          print("Cat meows")

a1  = Dog()
a2 = Cat()

a1.sound()
a2.sound()