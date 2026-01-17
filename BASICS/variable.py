# Rules for Naming Variables

# Can contain letters, digits, _
# Cannot start with digit
# No spaces
# Case-sensitive (age and Age different)

x = 10
name = "Nikhil"
pi = 3.14

print("x",x,type(x))
print("name "+name,type(name))
print("pi",pi,type(pi))

x  = 5
print("x",x,type(x))
x  = 6.8
print("x",x,type(x))
x = 'c'
print("x",x,type(x))


a , b , c = 10,20,30 #assigning multiple value
print(a,b,c)

a = b = c = 100 #assigning same value
print(a,b,c)