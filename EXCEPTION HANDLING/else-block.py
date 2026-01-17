# else runs only if no exception occurs.

try:
    a = int(input("Enter the value of a:"))
    b = int(input("Enter the value of b:"))
    print(f"Division:{a/b}")

except ZeroDivisionError:
    print("Cannot divide by zero!")

except ValueError:
    print("Invalid input! Enter numbers only.")

else:
    print("no error occurs")