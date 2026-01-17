# Write using w mode (overwrite)
# ⚠️ Note: This deletes old content and writes fresh.

filename = "D:\CODING\PYTHON\FILE HANDLING\demo.txt"

f = open(filename,'w')

f.write("Old content of demo.txt file is deleted and i am writing fress content\n")
f.write("Hello Python\n")
f.write("File Handling Example\n")

f.close()