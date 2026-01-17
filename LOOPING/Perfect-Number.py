#Perfect Number: Sum of its proper divisors (excluding itself) = the number itself
# number = 6
# Divisors: 1, 2, 3
# Sum = 1 + 2 + 3 = 6  Perfect number

num = int(input("Enter number: "))

sum_div = 0

for i in range(1, num):
    if num % i == 0:
        sum_div += i

if sum_div == num:
    print(num, "is a Perfect Number")
else:
    print(num, "is NOT a Perfect Number")
