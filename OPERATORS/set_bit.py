n = int(input("Enter number: "))
pos = int(input("Enter bit position: "))

result = n | (1 << pos)
print("After setting bit:", result)
