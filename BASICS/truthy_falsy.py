bool(0)        # False
bool(0.0)      # False
bool("")       # False
bool([])       # False
bool(())       # False
bool({})       # False
bool(None)     # False

# everything other then above is truthy

bool(1)        # True
bool(-5)       # True
bool("hi")     # True
bool([0])      # True


bool("False")  # True (because string not empty)

x = list((1,3,4,5)) #[1, 3, 4, 5]
print(x)
x = tuple("Nikhil") #('N', 'i', 'k', 'h', 'i', 'l')
print(x)

x = set("Nikhil") #{'k', 'i', 'l', 'N', 'h'}
print(x)

x = list("Nikhil") #['N', 'i', 'k', 'h', 'i', 'l']
print(x)

x = set([1,2,4,5,6,6,7,7])
print(x)

x = tuple([1,2,4,5,6,6,7,7])
print(x)

# Convert list of pairs → dict

obj = dict([("age",21),("name","Nikhil")])
print(obj) #{'age': 21, 'name': 'Nikhil'} 


# Convert two lists into dict
key = ["Name:","Age:","Roll:","Branch:"]
value = ["Nikhil",21,13,"CSE(AI)"]

obj = dict(zip(key,value))
print(obj) # {'Name:': 'Nikhil', 'Age:': 21, 'Roll:': 13, 'Branch:': 'CSE(AI)'}

