L = [1,2,3,4,5,5,6,7]

print(f"actual List:{L}") 

# remove(x): remove first occurrence
L.remove(5)
print(L) # [1, 2, 3, 4, 5, 6, 7]

# pop(i) : remove by index
L.pop(4)
print(L) # [1, 2, 3, 4, 6, 7]

# clear() : remove all
L.clear()
print(L)  # []