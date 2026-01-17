# One Parent → Many Children
class Parent:
    def common(self):
        print("Common method from Parent")

class Child1(Parent):
    def feature1(self):
        print("Feature of Child1")

class Child2(Parent):
    def feature2(self):
        print("Feature of Child2")

c1 = Child1()
c2 = Child2()

c1.common()
c1.feature1()

c2.common()
c2.feature2()
