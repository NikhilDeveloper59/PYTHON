# One Parent → One Child
# Parent → Child
class Parent:
    def show_parent(self):
        print("<----Parent class Method--->")

class Child(Parent):
    def show_child(self):
        print("<----Child class method---->")



c = Child()
c.show_child()
c.show_parent()


        
        