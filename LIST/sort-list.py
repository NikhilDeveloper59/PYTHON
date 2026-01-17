l = [5, 2, 9, 1]

print(l)
# Bubble Sort

n = len(l)
for i in range(0,n):
    for j in range(0,n-i-1):
        if(l[j] > l[j+1]):
            l[j], l[j+1] = l[j+1], l[j]


print(l)
