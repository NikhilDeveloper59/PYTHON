filename = "D:\CODING\PYTHON\FILE HANDLING\demo.txt"
copy_file_name = "D:\CODING\PYTHON\FILE HANDLING\coping.txt"

with open(filename,'r') as source:
    with open(copy_file_name,'w') as destination:
        destination.write(source.read())

print("✨🎉Copied Successfully!")