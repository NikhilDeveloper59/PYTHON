# Positional Arguments : Order matters.
def sub(a, b):
    return a - b

print(sub(10, 3))  # 7

# Keyword Arguments ; Order doesn’t matter.
def sub(a, b):
    return a - b

print(sub(b=3, a=10))  # 7

# Default Arguments : If value not passed → default used.

def greet(name="Guest"):
    print("Hello", name)

greet()
greet("Nikhil")

# *args (Multiple values)
def total(*args):
    return sum(args)

print(total(10, 20, 30, 40))

def avg(*argc):
    total = sum(argc)
    av = total/len(argc)
    return av

print(avg(1,2,3,4,5))

# **kwargs (Key-Value)
def info(**kwargs):
    for key,val in kwargs.items():
        print(key,"-->",val)


info(name="Nikhil",age=12,branch="CSE")