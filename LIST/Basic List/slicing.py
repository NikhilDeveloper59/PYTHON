L = [10,12.5,'Nikhil','A',True,[1,2,3]]

# slice: (start,stop,step)

print(L[:]) # [10, 12.5, 'Nikhil', 'A', True, [1, 2, 3]]
print(L[:3]) # [10, 12.5, 'Nikhil']
print(L[0:3]) # [10, 12.5, 'Nikhil']
print(L[::-1]) # [[1, 2, 3], True, 'A', 'Nikhil', 12.5, 10]
print(L[:0:-1]) # [[1, 2, 3], True, 'A', 'Nikhil', 12.5