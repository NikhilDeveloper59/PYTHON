# Magic methods are special built-in methods in Python that start and end with double underscore:
# __method__ that is why called it dunder/magic method

class Demo:
    # __init__() → Constructor : Object Initialization
    def __init__(self,x):
        self.x = x

    # Object Printing : __str__() → user-friendly string
    def __str__(self):
        return  f"Book name:{self.x}" 

    # Length of object : __len__()
    def __len__(self):
        return len(self.x)
    


# Arthmatic operator magic method
    # __add__() → +
    def __add__(self, other):
        return self.x + other.x
    
    # __sub__() → - 
    def __sub__(self, other):
        return self.x - other.x
    
    # __mul__() → *
    def __mul__(self, other):
        return self.x * other.x
    
    # __truediv__() --> /
    def __truediv__(self,other):
        return self.x / other.x

    # __floordiv__() --> //
    def __floordiv__(self,other):
        return self.x // other.x
    
    # __pow__() --> **
    def __pow__(self,other):
        return self.x ** other.x
    

# Comparison Magic Methods
    def __eq__(self, other):
        return self.x == other.x
    
    def __ne__(self, other):
        return self.x != other.x
    
    def __ge__(self, other):
        return self.x >= other.x
    
    def __le__(self, other):
        return self.x <= other.x
    
    def __gt__(self, other):
        return self.x > other.x
    
    def __lt__(self, other):
        return self.x < other.x




#  for Object printing
obj1 = Demo("Pyhon OOPs")
print(obj1)


#  for finding object length
obj2 = Demo(["Nikhil","Rohit","Mohit"])
print(len(obj2))

# For arthmatic operation
print(Demo(10)+Demo(5)) # __add__()
print(Demo(10)-Demo(5)) # __sub__()
print(Demo(10)*Demo(5)) # __mul__()
print(Demo(10)/Demo(5)) # __truediv__()
print(Demo(10)//Demo(5)) # __floordiv__()
print(Demo(10)**Demo(5)) # __pow__()


# for comparision operator
print(Demo(10)==Demo(10))
print(Demo(11)!=Demo(10))
print(Demo(17)>=Demo(10))
print(Demo(10)<=Demo(30))
print(Demo(14)>Demo(13))
print(Demo(12)<Demo(18))