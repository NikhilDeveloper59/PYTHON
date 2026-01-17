n = int(input("n="))

is_prime = True
if n < 2 :
    is_prime = False
else:
    for i in range(2,int(n//2 + 1)):
        if n % i == 0:
            is_prime = False
            break   

print("prime" if is_prime else "Not prime")
