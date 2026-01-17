d = dict(name="Nikhil",branch = "CSE",age = 21,roll = 13)

# Using key
print("<-------Using key-------->")
print(d["name"]) # Nikhil
print(d["branch"]) # CSE
print(d["age"]) # 21
print(d["roll"]) # 13

print("<------Using get()------->")

# Using get() (safe)
print(d.get("name"))
print(d.get("branch"))
print(d.get("age"))
print(d.get("roll"))