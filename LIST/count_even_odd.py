l = [10, 15, 20, 25, 30]
even = 0
odd = 0

for i in l:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even:", even)
print("Odd:", odd)
