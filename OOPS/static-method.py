class Calculator:

    @staticmethod
    def find(a,b):
        return a+b,a-b,a*b


add , sub, mul = Calculator.find(5,8)
print(f"add:{add}\nsub:{sub}\nmul:{mul}")
