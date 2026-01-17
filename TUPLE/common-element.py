tp1 = (1,4,6,8,3)
tp2 = (4,2,6,1,3)

common = tuple(set(tp1) & set(tp2))

print(common)