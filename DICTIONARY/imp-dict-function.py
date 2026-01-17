d = dict(name="Nikhil",branch = "CSE",age = 21,roll = 13)

print(d.keys())

print(d.values())

print(d.items())

# get(k) → safe access (no error)
print(d.get("age"))      # 21
print(d.get("salary"))   # None
print(d.get("salary", 0)) # 0 (default value)


d.update({"age": 22, "salary": 50000})
print(d)

d.pop("roll")
print(d)


# popitem() → remove last inserted key-value pair
d.popitem()
print(d)

d.clear()
print(d)
