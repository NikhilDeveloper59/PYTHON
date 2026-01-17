def print_fibo_series(n):
    a , b = 0 , 1
    for i in range(1,n+1):
        print(a,end=" ")
        a,b = b,a+b


n = int(input("n="))

print_fibo_series(n)