n = int(input("Enter number: "))
pos = int(input("Enter bit position: "))


if n & (1 << pos):
    print("Bit is SET")
else:
    print("Bit is NOT SET")