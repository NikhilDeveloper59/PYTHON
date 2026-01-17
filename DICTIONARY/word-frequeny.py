text = "python is easy and python is powerful"

l = text.split()
print(l)

freq = {}

for word in l:
    freq[word] = freq.get(word,0) + 1

for key,val in freq.items():
    print(key,"-->",val)