# finally runs always, whether exception happens or not
try:
    a = int(input("Enter the value of a:"))
    b = int(input("Enter the value of b:"))
    print(f"Division:{a/b}")

except Exception as e:
    print("Error is:{}".format(e))
finally:
    print("Execution completed. ")



