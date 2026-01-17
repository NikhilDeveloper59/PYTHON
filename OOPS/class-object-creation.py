class Student:

    college = "Government Engineering College"

    # Defoult constructor: it will automatically invoke when object is created 
    # self arguement is necessary for constructor of Methods --> self pointing current object 
    def __init__(self):
        self.name = "Nikhil Kumar"
        self.roll = 13
        self.age = 21

    # Method to show details 
    def show(self):
        print(f"College:{self.college}\nName:{self.name}\nRoll:{self.roll}\nAge:{self.age}")

# instance of class Student that means object
s1 = Student() # object s1 is created

s1.show()