class Student:
    college = "ABC college"

    def __init__(self,name):
        self.name = name
    
    @classmethod # necessary for class method
    def change_college(cls,new_name):
        cls.college = new_name
    

# Called using class:also possible using object, but best practice is class name

print(Student.college)
Student.change_college("XYZ college")
print(Student.college)


