students = {}

while True:
    print("\n1.Add  2.Display  3.Search  4.Delete  5.Exit")
    ch = int(input("Enter choice: "))

    if ch == 1:
        roll = int(input("Enter roll: "))
        name = input("Enter name: ")
        students[roll] = name
    elif ch == 2:
        print(students)
    elif ch == 3:
        roll = int(input("Enter roll to search: "))
        print(students.get(roll, "Not Found"))
    elif ch == 4:
        roll = int(input("Enter roll to delete: "))
        students.pop(roll, "Not Found")
    else:
        break
