L = [10,12.5,'Nikhil','A',True,[1,2,3]]

print(L)

# Change value using index
L[1] = 5
L[3] = "Raaz"

print(L)

# Replace multiple values

L[1:6] = [20,30,40,50,60]
print(L) # [10, 20, 30, 40, 50, 60]