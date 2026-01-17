a = "listen"
b = "silent"

freq1 = {}
freq2 = {}

for ch in a:
    freq1.get(ch) # count frequency of each char present in string a

for ch in b:
    freq2.get(ch) # count frequency of each char present in string b

# Method2: sort the both  string and check equal or not

print("Anagram" if freq1 == freq2 else "Not Anagram")