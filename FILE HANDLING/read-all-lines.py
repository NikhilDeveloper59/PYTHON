f = open("D:\CODING\PYTHON\FILE HANDLING\demo.txt","r")

# Read first line using readline()
all_line = f.readlines()
print("first line of file demo.txt is:\n",all_line)

f.close()