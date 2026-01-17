# OOP (Object Oriented Programming) is a programming style where we model real-world entities using:
    # Class → Blueprint
    # Object → Real instance of that blueprint

# Example:
#         Class: Car
#         Object: BMW, Audi

# Constructor: Constructor is called automatically when object is created.
# Types: Default Constructor ,Parameterized Constructor

# Instance vs Class Variables
    # Instance variable: unique for every object
    # Class variable: shared for all object

# Types of Methods
#1. Instance Method : 
    # An instance method works with object (instance) data.
    # It always takes self as the first parameter.
    # It can access:
    # --->instance variables (self.name)
    # --->class variables (ClassName.var)

# 2.Class Method :
    # A class method works with class-level data.
    # It uses decorator: @classmethod
    # It takes cls as the first parameter (represents class)
    # It is used when:
    # --->you want to modify/access class variables
    # --->you want alternative constructors

#3 Static Method
    # A static method is like a normal function inside a class.
    # It uses decorator: @staticmethod
    # It takes no self and no cls
    # Used when method:
    # --->does not need instance variables
    # --->does not need class variables
    # --->logically belongs to that class

# Access Modifiers
#     Modifier   	Syntax	    Meaning
#     Public	    name	accessible everywhere
#     Protected	    _name	child classes should access
#     Private	    __name	only inside same class

# Pillars of OOP
    # Encapsulation :Binding data + methods together inside class.
    # Inheritance:Child class gets properties of Parent class.
    # Polymorphism : Same function name, different behaviors.
    # Abstraction:Hiding internal implementation & showing required details.