# Python does not support method overloading directly (same name + different parameters)
# But we can achieve using: default arguments / *args

class Add:
    def __init__(self):
        pass

    def add_digit(self,a=0,b=0,c=0):
        return a+b+c

print(Add.add_digit(10,20))
print(Add.add_digit(10,20,30))
