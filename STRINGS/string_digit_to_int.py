s = "12345"

# finding ASCII value of character we use ord() function
# ord('0') = 48

num = 0

for ch in s:
    num = num * 10 + (ord(ch) - ord('0'))

print(num,type(num))