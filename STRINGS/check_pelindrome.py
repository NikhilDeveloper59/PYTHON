s = input("Enetr the string:")

rev = ""

for ch in s:
    rev = ch + rev

print("Pelindrome" if s == rev else "Not pelindrome")