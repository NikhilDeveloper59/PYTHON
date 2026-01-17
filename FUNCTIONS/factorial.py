def factorial_is(n):
    if( n<=0): return 1
    else: return n*factorial_is(n-1)

num = int(input("Enter number:"))
fact = factorial_is(num)

print(f"Factorial:{fact}")
