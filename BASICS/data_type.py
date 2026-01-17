# Numeric Types
x = 5  #int
print(x,type(x))

x = 5.6 #float 
print(x,type(x))

x = 5 + 7j #complex
print(x,type(x))

# Boolean Type

is_true = True
print(is_true,type(is_true))

# Truthy / Falsy:
is_true = "" # false
print(is_true,type(is_true))
is_true = [] # false
print(is_true,type(is_true))
is_true = 0  # false
print(is_true,type(is_true))
is_true = 1  # true
print(is_true,type(is_true))


# String Type (str)

name = "Nikhil"

print(name[0]) #print first char
print(name[-1]) # print last char
print(name[-2]) # print second last char
print(name[0:4]) # print 4 char from 0th index
print(name[::-1]) # reverse string


# Sequence Types
# list (Mutable)

list = [10,20,True,'a',"Nikhil",[1,2,3]]
print(list)
list.append("Kumar")
print(list)

# tuple (Immutable)
t = (1, 2, 3)
print(t[0])

# range

r = range(1,11) 
print(tuple(r))

# set (unordered, unique)

s = {1,2,3,4,5,5}
print(s,len(s)) 

# None Type: Means no value (null)
x = None
print(x)
print(type(x))


student = {
    "name:":"Nikhil Kumar",
    "age:":21,
    "Reg.No:":22151144031,
}
print(student)
print(student['name:'])
print(student['age:'])
print(student['Reg.No:'])
