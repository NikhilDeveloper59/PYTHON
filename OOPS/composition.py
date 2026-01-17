# Composition: Instead of inheritance, class contains object of another class.

class Engine:
    def start(self):
        print("start engine")

class Car:

    def __init__(self):
        self.engine = Engine() # user features of engine but not inherited
    
    def drive(self):
        self.engine.start()
        print("driving car")


c = Car()

c.drive()