# zip() is a built-in Python function that combines multiple lists/tuples/stringselement
# by element and creates pairs (tuples).

names = ["Amit", "Nikhil", "Rahul"]
marks = [90, 85, 88]

result = zip(names, marks)
print(list(result)) # [('Amit', 90), ('Nikhil', 85), ('Rahul', 88)]

for key,value in zip(names,marks):
    print(key,"-->",value)


students = ["A", "B", "C"]
math = [90, 70, 80]
english = [88, 75, 82]

for name,m,e in zip(students,math,english):
    print(name,"Math:",m,"English:",e)
