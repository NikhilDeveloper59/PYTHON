tp = (7,5,3,1,6,9,4,3)

print(tp)
lst = list(set(tp))
lst.sort()
tp = tuple(lst)

print(f"first max:{tp[-1]} and second max:{tp[-2]}")