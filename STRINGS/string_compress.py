s = "aaabbccccc"

freq = {}

for ch in s:
    freq[ch] = freq.get(ch,0) + 1

ans = ""
for key,value in freq.items():
    ans +=(key+str(value))
    print(key,"-->",value)


print(ans)