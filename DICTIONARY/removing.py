d = dict(name="Nikhil",branch = "CSE",age = 21,roll = 13)


d.pop("roll") # remove specific key
print(d)

del d["age"] # delete key
print(d)

d.clear()  # remove all
print(d)