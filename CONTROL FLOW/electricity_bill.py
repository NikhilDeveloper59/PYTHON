units = int(input("Enter total units consumed: "))

bill = 0

if units <= 100:
    bill = units * 1.5

elif units <= 200:
    bill = (100 * 1.5) + ((units - 100) * 2.5)

elif units <= 300:
    bill = (100 * 1.5) + (100 * 2.5) + ((units - 200) * 4.0)

else:
    bill = (100 * 1.5) + (100 * 2.5) + (100 * 4.0) + ((units - 300) * 5.0)

# Add fixed charge
bill += 50

# Add surcharge if bill > 500
if bill > 500:
    bill = bill + (bill * 0.10)

print("Total Electricity Bill = ₹", bill)
