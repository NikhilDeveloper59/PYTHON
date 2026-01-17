st = input("Enetr the string:").lower()
v = c = s = 0

for ch in st:
    if (ch in "aeiou"):
         v += 1
    elif ch == " ":
         s += 1
    else:
         c += 1

print(f"Vowel:{v}, Consonant:{c} , Space : {s}")