string = "Nikhil Kumar Raaz"

# st = string[::-1] 

rev = ""
# for i in range(1,len(string)+1):
#     rev += string[-i]

for ch in string:
    rev = ch + rev

print(f"Reversed:{rev}")