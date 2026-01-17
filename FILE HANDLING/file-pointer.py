# File Pointer / Cursor:
# ✅ tell() → current position of cursor
# ✅ seek(pos) → move cursor

filename = "D:\CODING\PYTHON\FILE HANDLING\demo.txt"

with open(filename,'r') as f:
    print(f.tell()) # curser position before read:0
    print(f.read(11)) # curser read 11 charecte
    print(f.tell()) # now curser position is 11
    f.seek(0) # move cuser back to start
    print(f.tell()) # 0
    print(f.read(4)) # curser read 4 char
    print(f.tell())
    f.seek(3) # curser move back to 3 char
    print(f.tell()) # 1
