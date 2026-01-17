tp  = (1,2,3,4,5)

print(tp)

print(tp[0]) # 1
print(tp[1]) # 2
print(tp[-1]) # 5
print(tp[-2]) # 4

# tp[0] = 5  tuple not mutable
# print(tp)


# But inside tuple if list exists → list can change:
tp = (1,2,3,[10,20],4)

print(tp[3])
tp[3][0] = 15
print(tp[3])