# Case Methods
s = "python developer"
print(s.upper())      # PYTHON DEVELOPER
print(s.lower())      # python developer
print(s.title())      # Python Developer
print(s.capitalize()) # Python developer


# Checking Methods
s = "Nikhil123"
print(s.isalpha()) # False
print(s.isdigit()) # False
print(s.isalnum()) # True (both alpha and number)
print(s.startswith('Nik')) # True
print(s.endswith('23'))  # True


# Finding & Replacing
s = "I love python"

print(s.find("python"))     # starting index
print(s.replace("python", "Java"))


# Strip / Remove Spaces
s = "   Hello   "

print(s.strip())     # removes leading & trailing spaces
print(s.lstrip())    # removes leading  spaces
print(s.rstrip())    # removes trailing spaces

# Split & Join
s = "apple,banana,mango"
list1 = s.split(",")
print(list1)

print("-".join(list1))
print(" ".join(list1))