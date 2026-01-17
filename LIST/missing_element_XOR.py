arr = [1, 2, 4, 5]
n = 5

x1 = x2 = 0

for i in range(1,n+1):
    x1 = x1 ^ i

for j in arr:
    x2 = x2 ^ j

missing = x1 ^ x2
print("Missing =", missing)