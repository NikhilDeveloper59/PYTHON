# Rotate list to RIGHT by k positions
# Example: [1,2,3,4,5], k=2 → [4,5,1,2,3]

l = [1, 2, 3, 4, 5]
k = 2

k = k % len(l) # handle k value larger than list size

l1 = l[0:-k] # [1,2,3]
l2 = l[-k:]  # [4,5]
l = l2 + l1  # [4, 5, 1, 2, 3]

print("Right Rotation:",l)


# Rotate list to LEFT by k positions
# Example: [1,2,3,4,5], k=2 → [3,4,5,1,2]
l = [1, 2, 3, 4, 5]

l1 = l[0:k] # [1,2]
l2 = l[k:] # [3,4,5]
l = l2 + l1
print("Left Rotation:",l)



