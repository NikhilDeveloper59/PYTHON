# Convert Tuple to List and Modify

tp = (1,2,3,4)
    
print(tp)
l = list(tp)
l.append(5) 
tp = tuple(l)

print(tp)