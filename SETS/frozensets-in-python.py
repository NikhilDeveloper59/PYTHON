fs = frozenset([1, 2, 3, 3, 4])

print(fs) # frozenset({1, 2, 3, 4})

frozenset({1, 2, 3, 4})

# cannot change
# fs.add(4)        #  AttributeError
# fs.remove(2)     #  AttributeError


A = frozenset([1, 2, 3, 4])
B = frozenset([3, 4, 5, 6])

# Allowed Operations on frozenset
print(A | B)   # union
print(A & B)   # intersection
print(A - B)   # difference
print(A ^ B)   # symmetric difference


# As dictionary key
d = {
    frozenset([1, 2]): "Group A",
    frozenset([3, 4]): "Group B"
}
print(d)

#  simple sets not use as key
# d = {  
#     {1,2}: "Group A",
#     {3,4}: "Group B"
# }


# s = {1,2,{3,4}} not allowed
s = {1,2,frozenset([3,4])} 
print(s)

