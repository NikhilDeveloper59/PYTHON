# It gives both position (index) and  element (value)

arr = ["A", "B", "C"]

# Without enumerate:
for i in range(len(arr)):
    print(i, arr[i])


# With enumerate
arr = ["A", "B", "C"]

for index, value in enumerate(arr):
    print(index, value)
