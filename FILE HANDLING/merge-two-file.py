with open("file1.txt", "r") as f1:
    data1 = f1.read()

with open("file2.txt", "r") as f2:
    data2 = f2.read()

with open("merge.txt", "w") as f3:
    f3.write(data1 + "\n" + data2)

print(" Files merged successfully into merge.txt")
