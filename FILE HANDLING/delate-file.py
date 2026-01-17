import os

filename = "D:\CODING\PYTHON\FILE HANDLING\deliting-file.txt"

if os.path.exists(filename):
    os.remove(filename)
    print("File Deleted ✅")
else:
    print("File not found ❌")