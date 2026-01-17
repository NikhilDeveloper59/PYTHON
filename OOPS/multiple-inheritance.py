# Multiple Parents → One Child

class Father:
    def father_skill(self):
        print("Father: Driving")

class Mother:
    def mother_skill(self):
        print("Mother: Cooking")

class Child(Father,Mother):
    def child_skill(self):
        print("Child: Coding")

#  child inherit both mother and father data and methods
c = Child()
c.child_skill()
c.mother_skill()
c.father_skill()