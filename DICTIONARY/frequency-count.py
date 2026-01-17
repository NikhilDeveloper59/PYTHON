s = "programming"

freq = {}

for ch in s:
    freq[ch] = freq.get(ch,0)+1

for key,val in freq.items():
    print(key,"-->",val)