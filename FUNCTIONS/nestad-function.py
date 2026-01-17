def outer():
    def inner():
        print("Inner function")
    print("Outer function")
    inner()

outer()
