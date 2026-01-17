class Student:
    # class variable : college shared for all objects
    college = "ABC college name"

    def __init__(self,name,marks):
        # instance variable : this will unique for every object 
        self.name = name
        self.marks = marks

# object 
s1 = Student("Nikhil",96)
print(f"College:{s1.college}\nName:{s1.name}\nMarks:{s1.marks}")

