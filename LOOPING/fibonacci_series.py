# 0,1,1,2,3,5,8,13,..........
# F(n)=F(n−1)+F(n−2)

n = int(input("Enter number of terms: "))

a, b = 0, 1

print("Fibonacci Series:")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

# Explanation: a, b = b, a + b
# a stores current Fibonacci number
# b stores next Fibonacci number
# update happens like:
#         a becomes b
#         b becomes a+b

i = 1
a, b = 0, 1
print()

while(i<=n):
    print(a,end=",")
    a , b = b , a+b
    i+=1
