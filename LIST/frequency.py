l = [1,2,2,5,6,5,8,9,6]

freq = {}
for i in l:
    freq[i] = freq.get(i,0)+1

for key,value in freq.items():
    print(key,"-->",value)