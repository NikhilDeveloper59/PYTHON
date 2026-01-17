s = "Programming"

# Method 1: convert into set but char order is different
# print(set(s)) 

temp = ""

for ch in s:
    if ch not in temp:
        temp +=ch
    else:
        continue

print(temp)