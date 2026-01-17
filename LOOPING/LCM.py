# smallest number divisible by both numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

gcd = 1
for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        gcd = i

lcm = (a * b) // gcd # formula

print("GCD =", gcd)
print("LCM =", lcm)
