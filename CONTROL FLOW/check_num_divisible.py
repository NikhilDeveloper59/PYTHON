# Check divisible by 5 and 11

n = int(input("n="))

if n % 5 == 0 and n % 11 == 0:
    print("Given number ",n," is divible by both 5 and 11")
elif (n % 5 == 0):
    print("Given number ",n," only divisible by 5")
elif (n % 11 == 0):
    print("Given number ",n," only divisible by 11")
else:
    print("Given number ",n," not divisible by 5 and 11")


    