    #   A
    #  / \
    # B   C
    #  \ /
    #   D

class A:
    def showA(self):
        print("A")

class B(A):
    def showB(self):
        print("B")

class C(A):
    def showC(self):
        print("C")

class D(B, C):
    def showD(self):
        print("D")

obj = D()
obj.showA()
obj.showB()
obj.showC()
obj.showD()
