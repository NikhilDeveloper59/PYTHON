arr = [1,2,2,3,4,4,5]

d = {}

for x in arr:
    d[x] = d.get(x,0) + 1

duplicate = {key for key,val in d.items() if val > 1}

print(duplicate)