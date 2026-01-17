def get_rev(num):
    rev = 0
    while num>0:
        digit = num % 10
        rev = rev*10 + digit
        num //=10
    return rev

print(get_rev(1234))
print(get_rev(847569))
print(get_rev(8647))