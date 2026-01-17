A = {1, 2, 3, 4}
B = {3, 4, 5, 6}


print(A | B)   # Union 

print(A & B)   # Intersection(common)


print(A - B)   # Difference


# A ^ B gives the elements which are present in either A or B BUT NOT in bot
print(A ^ B)   # Symmetric Difference: common elements removed, only different elements remain

print((A - B) | (B - A)) # A ^ B same