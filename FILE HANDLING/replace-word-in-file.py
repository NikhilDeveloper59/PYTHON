
filename = "D:\CODING\PYTHON\FILE HANDLING\demo.txt"

#  for searching the word in file
with open(filename,'r') as file:
     content = file.read()
     content = content.replace("Python","C++") # ("old", "new") --> this will replaice in content not in the file so write this content into file

with open(filename,'w') as f:
     f.write(content)

print("Python word replaced with C++ successfully✨")

 
