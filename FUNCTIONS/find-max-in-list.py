def find_max(arr):
    mx = arr[0]
    for i in arr:
        if i > mx:
            mx = i
    return mx

print(find_max([10, 45, 22, 99, 34]))
