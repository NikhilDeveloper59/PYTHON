l = [1,5,3,4,7,9,3,7]

print(l)
# l.reverse()

L = []

# for i in l[::-1]:
#     L.append(i)

# l  = L.copy()
# print(l)

for i in range(len(l)-1, -1, -1):
    L.append(l[i])

print(L)
