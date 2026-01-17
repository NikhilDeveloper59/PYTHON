from abc import ABC , abstractmethod    

class Bank(ABC):
      
    def __init__(self):
            pass
    
    @abstractmethod
    def deposit(self,amount):
          pass
    
    @abstractmethod
    def withdraw(self,amount):
          pass

class SBI(Bank):
    def deposit(self, amount):
        print("Deposited:", amount)
        
    def withdraw(self, amount):
        print("withdraw",amount)

acc = SBI()
acc.deposit(5000)
acc.withdraw(3500)