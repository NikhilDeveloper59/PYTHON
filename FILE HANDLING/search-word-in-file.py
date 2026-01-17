
filename = "D:\CODING\PYTHON\FILE HANDLING\demo.txt"

with open(filename,'r') as file:
    text = file.read().lower()
    key = "Python"

    if key.lower() in text:
        print(f"{key} word exist in the file 🥰")
    else:
        print(f"{key} word not exist in the file😓")

