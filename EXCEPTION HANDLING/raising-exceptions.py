# raise: You can create your own error.

age = int(input("Enter the age:"))

if age < 18:
    raise ValueError("Age must be 18 or above!")
else:
    print("Eligible")