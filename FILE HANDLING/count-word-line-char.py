
filename = "D:\CODING\PYTHON\FILE HANDLING\demo.txt"

with open(filename,'r') as file:
    text = file.read()

    print(f"total character in the file is:{len(text)}")
    words = text.split(" ")
    print(f"Number of words in the file is:{len(words)}")
    print(f"Number of line in the file is:{text.count('\n')}")

print("🎁🎉I have successfully conting char/words/line")