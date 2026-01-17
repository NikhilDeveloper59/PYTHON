a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

if a > b:
    if a > c:
        print("Largest is:", a)
    else:
        print("Largest is:", c)
else:
    if b > c:
        print("Largest is:", b)
    else:
        print("Largest is:", c)
