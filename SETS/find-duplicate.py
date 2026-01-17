# Find duplicates in list using set
lst = [1, 2, 3, 2, 4, 1, 5]

seen = set()
duplicate = set()

for x in lst:
    if x in seen:
        duplicate.add(x)
    else:
        seen.add(x)

print(duplicate)