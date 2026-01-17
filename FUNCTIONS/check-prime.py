def is_prime(n):
    for i in range(2,n//2+1):
        if(n%i==0):
            return False
    return True


n = int(input("n="))
if is_prime(n):
    print("This is prime")
else:
    print("Not a prime")