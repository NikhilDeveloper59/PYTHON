class Student:
    def __init__(self):
        print("Defoult constructor called auto")
    
    def __init__(self,name,marks,age):
        self.names = name
        self.marks = marks
        self.age = age
    
    def show(self):
        print(f"name:{self.names}  Marks:{self.marks}  Age:{self.age}")

s1 = Student("Nikhil Kumar",85,34)
s2 = Student("Mohit Kumar",95,14)
s3 = Student("Rohit Kumar",65,21)


s1.show()
s2.show()
s3.show()