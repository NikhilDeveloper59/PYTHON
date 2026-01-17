def get_sum(num):
    sum = 0
    while num>0:
        digit = num % 10
        sum += digit
        num //=10
    return sum

print(get_sum(1234))
print(get_sum(847569))
print(get_sum(8647))