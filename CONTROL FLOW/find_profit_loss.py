# Find profit/loss
cost_prise = int(input("Enter the cost prise:"))
selling_prise = int(input("Enter the selling prise:"))

diff = selling_prise - cost_prise

if diff > 0:
    print("Profit of ",diff," rupee")
elif diff < 0:
    print("Loss of ",-diff," rupee")
else:
    print("No profit No loss")