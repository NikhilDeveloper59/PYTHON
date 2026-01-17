a = int(input("Enter a: "))
b = int(input("Enter b: "))

op = input("Enter operator (+,-,*,/): ")

match op:
    case "+":
        print("sum:",a+b)
    case "*":
        print("Product:",a*b)
    case "-":
        print("Difference:",a-b)
    case "/":
        print("Division:",a/b)
    case _:
        print("Invalid Oprator")
    