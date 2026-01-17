list = [1,2,3,5,6,7]
n = 7

missing = set(range(1,n+1)) - set(list)

print(missing)