# Used to create list in single line , Faster than loops
# Syntax: new_list = [expression for item in iterable]

num = [1,2,3,4,5]
print(num) # [1, 2, 3, 4, 5


square = [x*x for x in num]
print(square) #[1, 4, 9, 16, 25]


odd  = [x for x in range(1,11,2)]
print(odd)

even = [ x for x in range(2,11,2)]
print(even)

# List Comprehension with Condition (IF)

even = [x for x in range(2,21) if x % 2 == 0]
print(even)

# List Comprehension with Condition (IF-ELSE)
l = ["Even" if x % 2 == 0 else "Odd" for x in range(1, 11)]
print(l)


# Extract Only Positive Numbers

nums = [-10, 20, -5, 15, -2, 7]

pos = [x for x in nums if x > 0]
print(pos)
