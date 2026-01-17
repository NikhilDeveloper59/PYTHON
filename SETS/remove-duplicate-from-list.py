# Remove duplicates while maintaining order

lst = [10, 20, 10, 30, 20, 40]

seen = set()
ans = []

for x in  lst:
    if x not in seen:
        seen.add(x)
        ans.append(x)

print(ans)