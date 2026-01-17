def get_power(a,b):
    if(b==1): return a
    else:
        return a*get_power(a,b-1)

print(get_power(2,4))
print(get_power(3,3))
print(get_power(5,3))