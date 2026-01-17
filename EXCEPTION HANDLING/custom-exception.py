# Custom Exceptions (User-Defined Exception)
#  you can create their own custom exception handler

class NegativeValueError(Exception):
    pass

try:
   num = int(input("Enter the number:"))

   if(num < 0):
       raise NegativeValueError("Negative number not allowed!")
   else:
       print("Number is:",num)

except NegativeValueError as e:
      print(f"Error:{e}")