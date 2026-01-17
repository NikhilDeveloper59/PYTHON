# strong number: Sum of factorial of each digit = original number
# 145 = 1! + 4! + 5! = 1 + 24 + 120 = 145

num = int(input("Enter number: "))
temp = num
sum_fact = 0

while temp > 0:
    digit = temp % 10
    # Factorial find
    fact = 1
    for i in range(digit,0,-1):
        fact *=i

    sum_fact += fact
    temp //= 10

if sum_fact == num:
    print(num, "is a Strong Number")
else:
    print(num, "is NOT a Strong Number")
