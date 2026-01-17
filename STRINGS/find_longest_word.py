s = "I love python programming language"

words = s.split(" ")

n = len(words)
max = len(words[0])
idx = 0

for i in range(1,n):
    if(max < len(words[i])):
        max = len(words[i])
        idx = i

print(f"longest word:{words[idx]} of length:{len(words[idx])}")

