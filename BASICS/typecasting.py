x = "10"
print(x,type(x))

x = 5 + int(x) # type cast str --> int

print(x,type(x))

# common implicit conversions:
# int → float   
# bool → int
# int → complex

a = 10      # int
b = 2.5     # float
c = a + b   # int automatically converts to float
print(c,type(c))  #12.5 , float


x = int("10")     # 10
print(x,type(x))
x = int(10.9)     # 10 (decimal removed)
print(x,type(x))
x = int(True)     # 1
print(x,type(x))
x = int(False)    # 0
print(x,type(x))


# int("10.5")   # ValueError
# int("abc")    # ValueError

float("10")     # 10.0
float("10.5")   # 10.5
float(10)       # 10.0
float(True)     # 1.0

str(10)        # "10"
str(10.5)      # "10.5"
str(True)      # "True"

