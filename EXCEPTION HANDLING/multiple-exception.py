# Multiple Exceptions in One except

try:
    a = int(input("Enter the value of a:"))
    b = int(input("Enter the value of b:"))
    print(f"Division:{a/b}")

except (ZeroDivisionError,ValueError):
    print("Invalid input or division by zero!")




