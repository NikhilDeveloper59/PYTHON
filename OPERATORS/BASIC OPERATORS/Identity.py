a = 10
b = 10
c = a

# Checks memory location (object identity), not value.

print(a == b)
print(a is b) # true location of a and b same 
print(a is not b)
print(a is c)


a = [1,2]
b = [1,2]
c = a
print(a == b)  # True (value same)
print(a is b) # False (different objects)
print(a is not b) # true
print(c is a)