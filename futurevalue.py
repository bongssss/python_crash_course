# Initialize variables
total_fv = 0
annual_rate = 0.07  # Annual return rate of 7%
monthly_rate = (1 + annual_rate) ** (1 / 12) - 1  # Compounded monthly rate
n = 15 * 12  # Total number of months (15 years)

# Loop through each month, calculating the future value of each month's investment
for month in range(1, n + 1):
    # Calculate the monthly investment
    monthly_investment = 200 + (month - 1) * 100
    
    # Calculate the future value of this month's investment
    fv_of_monthly_investment = monthly_investment * (1 + monthly_rate) ** (n - month)
    
    # Add it to the total future value
    total_fv += fv_of_monthly_investment

total_fv

print(total_fv)

