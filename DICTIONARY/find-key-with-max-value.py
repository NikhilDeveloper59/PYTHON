d = {"a": 10, "b": 99, "c": 55}

key = max(d,key=d.get)
print(d[key])