# File handling means:
# ✔ creating, opening, reading, writing, updating and deleting files using Python.

# Python provides built-in functions for file operations:
# open() ,read(), readline(), readlines(),write(), writelines(),close(),etc

# Opening a File in Python

file_object = open("file_name","mode")

# common modes is 

# Modes           Meaning
# r               read(defoult)
# w               write (Overwrite)
# a               Append (add new content)
# x               create a new file
# rb              read bynary 
# wb              write bynary 
# r+              read + write
# w+              write + read(overwrite)
# a+              append + read

# with statement more used becouse no need to write close() file it automaticlly close the file
# with open("file_name","mode") as f:
#       data = f.read()
#       print(data)





# demo.txt file before write

# <---------You are open domo.txt file --------->

# Why did the bicycle fall over?
# Because it was two tired! (A pun on "too tired")
# ✔This file is used for file handling purpose 
