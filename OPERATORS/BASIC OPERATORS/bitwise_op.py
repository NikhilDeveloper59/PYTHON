a = 5   # 0101
b = 3   # 0011

print(a & b)   # 1  (0001)
print(a | b)   # 7  (0111)
print(a ^ b)   # 6  (0110)
print(~a)      # -6 (1010) => -8 + 2 = -6 first 1 of binary number tells sign of number
print(a << 1)  # 10 (1010) 5*2 = 10
print(a >> 1)  # 2  (0101) 5//2 = 2
