# Exception as e :This gives the exact error message.
try:
    a = int(input("Enter the value of a:"))
    b = int(input("Enter the value of b:"))
    print(f"Division:{a/b}")

except Exception as e:
    print(f"Error:{e}")



