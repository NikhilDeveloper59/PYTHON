n = int(input("Enter number:"))

fact = 1
# for i in range(n,0,-1):
#     fact *= i

i = 1 
while i <= n:
    fact *= i
    i +=1
print("factorial:",fact)