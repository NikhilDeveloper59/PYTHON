# Conditions:
# Withdrawal amount must be multiple of 100
# Amount must be greater than 0
# Amount must be less than or equal to balance
# Minimum balance must remain after withdrawal (₹500)

balance = float(input("Enter your account balance: "))
withdraw = float(input("Enter withdrawal amount: "))

min_balance = 500

if withdraw <= 0:
    print("Invalid amount! Enter amount greater than 0.")

elif withdraw % 100 != 0:
    print("Withdrawal amount must be in multiples of 100.")

elif withdraw > balance:
    print("Insufficient balance!")

elif balance - withdraw < min_balance:
    print("Cannot withdraw! Minimum balance of ₹500 must be maintained.")

else:
    balance = balance - withdraw
    print("Withdrawal successful ")
    print("Remaining Balance: ₹", balance)
