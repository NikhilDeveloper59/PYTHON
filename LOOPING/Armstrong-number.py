num = int(input("Enter number:"))

# count digits in num
count = len(str(num))

# count = 0
# n = num
# while n > 0:
#     count +=1
#     n //=10

n = num
temp = 0
while(n>0):
    digit = n % 10
    temp +=(digit**count) 
    n //=10

print("Armstrong" if temp == num else "Not Armstrong")