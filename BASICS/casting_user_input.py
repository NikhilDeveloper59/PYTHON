# By defoult input return string(str)
x = input("Enter number: ")
print(type(x))   # str

x = int(input("Enter number: "))
print(type(x))   # int

x = float(input("Enter number: "))
print(type(x))   # float

binary = int("1010",2) # 1010 = 10 is a binary number (base:2)
print(binary)

binary = int("1010",8) # 1010 = 520 is a octal number (base:8)
print(binary)

binary = int("1010",10) 
print(binary)