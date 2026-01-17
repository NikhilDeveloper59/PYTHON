# Annual Income        Tax Rate 
# Up to 2,50,000        0%      
# 2,50,001 – 5,00,000   5%       
# 5,00,001 – 10,00,000  20%      
# Above 10,00,000       30%      

income = float(input("Enter your annual income: "))

tax = 0

if income <= 250000:
    tax = 0

elif income <= 500000:
    tax = (income - 250000) * 0.05

elif income <= 1000000:
    tax = (250000 * 0.05) + (income - 500000) * 0.20

else:
    tax = (250000 * 0.05) + (500000 * 0.20) + (income - 1000000) * 0.30

print("Total Income Tax = ₹", tax)

