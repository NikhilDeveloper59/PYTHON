class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def show(self):   # Instance Method
        print("Name:", self.name)
        print("Marks:", self.marks)

s1 = Student("Nikhil", 90)
# Called using object:
    
s1.show()
