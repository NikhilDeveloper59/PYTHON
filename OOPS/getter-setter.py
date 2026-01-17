# Property Decorators (Getter/Setter)
# @property lets you access a method like an attribute. used to implement getter/setter
# So you can write: obj.age instead of  obj.get_age()

class Person:

    def __init__(self,age):
        self._age = age # protected variable
    
    
    @property
    def age(self):     # Getter
        return self._age
    
    @age.setter
    def age(self,value):  # Setter
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value



p = Person(10)
print(p.age)

p.age = 25       # calls setter

print(p.age)
