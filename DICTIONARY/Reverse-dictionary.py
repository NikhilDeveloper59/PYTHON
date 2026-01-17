# Reverse dictionary (swap keys and values)

d = {"a": 1, "b": 2, "c": 3}

print(d)

reverse = {value: key for key,value in d.items()}

print(reverse)