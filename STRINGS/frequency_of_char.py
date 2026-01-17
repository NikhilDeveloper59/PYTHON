s = input("Enetr the string:")

# Using Dictionary
freq = {}

for ch in s:
    if ch in freq:
        freq[ch] +=1
    else:
        freq[ch] = 1

print(f"Frequency:{freq}")

# less use
# for ch in set(s):
#     print(ch, ":", s.count(ch))



for ch in s:
    freq[ch] = freq.get(ch,0) + 1

print(f"Frequency:{freq}")



