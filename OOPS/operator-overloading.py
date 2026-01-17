# Operator Overloading
# Same operator behaves differently for different objects
# (Using magic methods like __add__, __mul__)


class Demo:
    def __init__(self,x):
        self.x = x

    def __add__(self,other):
        return self.x + other.x
    
    def __mul__(self,other):
        return self.x * other.x



print(Demo(5) + Demo(6))
print(Demo(5) * Demo(6))
        