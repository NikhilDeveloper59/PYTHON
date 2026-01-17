# A → B → C

class GrandParent:
    def show_gp(self):
        print("<----GrandParent called--->")

class Parent(GrandParent):
    def show_p(self):
        print("<-----Parent called ------>")

class Child(Parent):
    def child_c(self):
        print("<------Child called------>")

obj = Child()
obj.show_gp()
obj.show_p()
obj.child_c()