# Encapsulation: Binding data + methods together inside class.

class Bank:
    def __init__(self,amount):
        self.__balance = amount # private
    
    def view_balance(self):
        print(f"Your current balance is:{self.__balance}")
    
b = Bank(5000)
b.view_balance()


# '__balance' becomes private

