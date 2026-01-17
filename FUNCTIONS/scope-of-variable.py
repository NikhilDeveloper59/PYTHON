x = 100  # global

def show():
    x = 20  # local
    print("Inside:", x)

show()
print("Outside:", x)


# Using global keyword
x = 10

def change():
    global x
    x = 50

change()
print(x)  # 50