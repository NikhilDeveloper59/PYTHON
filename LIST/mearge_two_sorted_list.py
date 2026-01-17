a = [1, 3, 5, 7]
b = [2, 4, 6, 8]

i = j = 0 
merge = []
n1 = len(a)
n2 = len(b)
 
while i < n1 and j < n2:
    if(a[i] < b[j]):
        merge.append(a[i])
        i += 1
    else:
        merge.append(b[j])
        j += 1

# add remaing element
while i < n1:
    merge.append(a[i])
    i += 1

while j < n2:
    merge.append(b[j])
    j += 1

print(merge)